# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:02:58 2019
与当前的cmd进行交互 sys
@author: dell
"""
import re
import os
import sqlite3
import pymysql
import time
import threading
import sys
import json
import redis
from Film135Zy import Film135Zy

class FilmAction:
    '''
    def test_db() 测试数据库是否存在
    def work() 将网站电影全部写入数据库
    def my_thread() 开启多线程写入数据库中
    '''
    def __init__(self,film_object):
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '',
            'db':'aa',
            'charset':'utf8'
        # =============================================================================
        # 
        #     # 创建游标，查询获得的数据以 字典（dict） 形式返回
        #     'cursorclass':pymysql.cursors.DictCursor
        # =============================================================================
            }
        self.film_object=film_object
        self.r = redis.StrictRedis(host='192.168.2.119',port='6379',decode_responses=True)
        print('redis初始化完成')
        #支持多线程操作
#        self.conn = sqlite3.connect('film.sqlite3',check_same_thread=False)
#        self.cursor = self.conn.cursor()
        self.conn = pymysql.connect(**self.config)
        self.cursor = self.conn.cursor()
        print('数据库初始化完成')
        #创建锁
        self.cursor_lock=threading.Lock()
        self.test_db()
        self.iter_get_all_page_url=self.film_object.get_all_show_page_url_yield()

    def test_db(self):
        create_sql = '''\
        
            CREATE TABLE IF NOT EXISTS film_infos(
            
                    id INTEGER PRIMARY KEY auto_increment,
                    
                    name TEXT,
                    
                    url  varchar(255) UNIQUE,
                    
                    update_time  TEXT,
                    
                    types  TEXT,
                    
                    status TEXT NULL
            
            )'''
        ##获取锁
        self.cursor_lock.acquire()
        
        self.cursor.execute(create_sql)
        self.conn.commit()
        
        ##释放锁,一定要释放锁,否则会成死线程
        self.cursor_lock.release()
    
    def work(self):
        
        insert_sql = '''
        
            INSERT INTO film_infos
            
            (name ,url , update_time ,types)
            
            VALUES
            
            (%s ,%s ,%s ,%s)'''
        while True:
            show_page_url=next(self.iter_get_all_page_url)
            try:
                info=self.film_object.get_show_page_info(show_page_url)
            except:
                self.r.set(show_page_url,str(sys.exc_info()))
                print('出错啦',show_page_url)
            else:
                insert_list=[(i['href'],i['name'],i['types'],i['update_time']) for i in info['film_list']]
                self.cursor_lock.acquire()
                try:
                    self.cursor.executemany(insert_sql,insert_list)
                except pymysql.IntegrityError as err:
                    print(err.args)
                    print(show_page_url,'已经存在')
                    self.cursor_lock.release()
                else:
                    self.conn.commit()
                    print(show_page_url)
                    self.cursor_lock.release()
     
    def my_thread(self):
        for i in range(5):
            t=threading.Thread(target=self.work)
            t.start()
            
    def search_detail(self,keyword,page=None):
        if page==None:
            page=0
        search_info=self.film_object.film_search(keyword)['search_list'][page*5:(page+1)*5]
        detail_search_list=[]
        def run(url):
            detail_search_list.append(self.film_object.get_film_info(url))
        threads=[]
        for i in range(5):
            try:
                url=search_info.pop()['url']
            except IndexError:
                print('search_detail,任务队列完成')
                break
            else:
                t=threading.Thread(target=run,args=(url,))
                threads.append(t)
                t.start()
        for i in threads:
            t.join()
        self.r.set(keyword,json.dumps({'info':detail_search_list},ensure_ascii=False))
        return {'info':detail_search_list}
    
    def search_detail_redis(self,keyword):
        if self.r.exists(keyword):
            return json.loads(self.r.get(keyword))
        else:
            return self.search_detail()
    
    #获取文件夹下面的所有文件
    def get_fileList(self,dirs,fileList):
        files=os.listdir(dirs)
        for file in files:
            fileList.append(file)
        return fileList
    
if __name__ == '__main__':
    
    
    x=FilmAction(Film135Zy())
#    xiangqing=x.work()
    





























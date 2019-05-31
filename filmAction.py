# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:02:58 2019
与当前的cmd进行交互 sys
@author: dell
"""
import re
import sqlite3
import pymysql
import time
import threading
import sys
import json
import redis
import requests
from spider2 import Spider
class FilmAction:
    '''
    def test_db() 测试数据库是否存在
    def work() 将网站电影全部写入数据库
    def my_thread() 开启多线程写入数据库中
    '''
    def __init__(self,film_object):
        
        self.film_object=film_object
        self.r = redis.StrictRedis(host='192.168.2.119',port='6379',decode_responses=True)
        #支持多线程操作
        self.conn = sqlite3.connect('film.sqlite3',check_same_thread=False)
        self.cursor = self.conn.cursor()
        #创建锁
        self.cursor_lock=threading.Lock()
        self.test_db()
        self.iter_get_all_page_url=self.film_object.get_all_show_page_url_yield()

    def test_db(self):
        create_sql='''CREATE TABLE IF NOT EXISTS film_info(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    url  TEXT UNIQUE,
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
        
        insert_sql='''
            insert into film_info(name,url,update_time,type) values(?,?,?,?)
        '''
        while True:
            show_page_url=next(self.film_object.iter_get_all_page_url)
            try:
                info=self.film_object.get_page_film(show_page_url)
            except:
                self.redis.set(show_page_url,str(sys.exc_info()))
                print('出错啦',show_page_url)
            else:
                insert_list=[(i['name'],i['url'],i['update_time'],i['types']) for i in info]
                self.cursor_lock.acquire()
                try:
                    self.cursor.executemany(insert_sql,insert_list)
                except sqlite3.IntegrityError:
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
        self.r.set(keyword,json.dumps({'info':detail_search_list}))
        return {'info':detail_search_list}
    
    def search_detail_redis(self,keyword):
        if self.r.exists(keyword):
            return json.loads(self.r.get(keyword))
        else:
            return self.search_detail()

if __name__ == '__main__':
    from FilmSubo8988 import FilmSubo8988
    x=FilmAction(FilmSubo8988())
    xiangqing=x.search_detail('倚天屠龙记')








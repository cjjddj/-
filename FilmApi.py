# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:12:06 2019

@author: dell
"""

import sys
sys.path.append('trait')
import redis
import importlib
import queue
import threading
import json
from script_trait import trait_info
trait_info=trait_info()

class FilmApi:
    def __init__(self):
        pool=redis.ConnectionPool(host='192.168.2.119',port=6379,decode_repsonses=True)
        self.r=redis.StrictRedis(connection_pool=pool)
        self.q=queue.Queue(5)
        self.search_info={}
        
    def film_search(self,keyword):
        class_list=[]
        for i in trait_info:
            trait=importlib.import_module(i.replace('trait\\','').replace('.py',''))
            class_list.append(getattr(trait,trait_info[i]))
        return [i().film_search(keyword) for i in class_list]
            
    ##生产者
    def productor(self):
         for i in trait_info:
             trait=importlib.import_module(i.replace('trait\\','').replace('.py',''))
               self.q.put(getattr(trait,trait_info[i]))
       
    #消费者
    def consumer(self,keyword):
        while True:
            task=self.q.get()
            if task == None:
                break
            #计数器
            task_class=task()
            try:
                info=task_class.film_search(keyword)
            except:
                '''向任务已经完成的队列发送一个信号'''
                self.q.task_done()
                print(task_class.domain,'失败')
            else:
                self.search_info[task_class.domain]=info
                print(task_class.domain,'完成')
                self.q.task_done()

            
            
            
            
            
            
            
            
            
            
            
            
            
            
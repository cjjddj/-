# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:19:48 2019

@author: dell
"""
from pymongo import MongoClient
import redis
mongo_host='192.168.2.119'
mongo_port=27017

redis_host='192.168.2.119'
redis_port=6379

mongo_conn=MongoClient(mongo_host,mongo_port)
pool=redis.ConnectionPool(host=redis_host,port=redis_port,decode_responses=True)
redis_conn=redis.StrictRedis(connection_pool=pool)
class DBConnect:
    
    instance=None  #记录第一个被创建对象的引用
    init_flag=False  #记录是否执行过初始化动作
    
    def __new__(cls,*args,**kwargs):
        
        if cls.instance is None: #判断类属性是否为空对象
            cls.instance=super().__new__(cls)  ##调用父类的方法为第一个对象分配空间
        return cls.instance #返回类属性保存的对象引用
    
    def __init__(self):
        
        if not DBConnect.init_flag:
            self.mongo_conn=MongoClient(mongo_host,mongo_port)
            pool=redis.ConnectionPool(host=redis_host,port=redis_port,decode_responses=True)
            self.redis_conn=redis.StrictRedis(connection_pool=pool)
            DBConnect.init_flag=True

if __name__ == '__main__':
    x=DBConnect()
         
用户名id,名称,性别,

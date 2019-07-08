# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:25:40 2019

@author: dell
"""

import multiprocessing
import importlib
import threading
import sys
sys.path.append('trait')
from setting import DBConnect
from script_trait import trait_info
trait_info=trait_info()
redis_conn=DBConnect().redis_conn

class ShowPageQueue:
    def __init__(self):
        self.trait_class_list=self.task_trait_class_list()
        
    @staticmethod
    def task_trait_class_list():
        class_list=[]
        for i in trait_info:
            trait=importlib.import_module(i.replace('trait\\','').replace('.py',''))
            class_list.append(getattr(trait,trait_info[i]))
        return class_list
    
    @staticmethod
    def task_trait_class_list():
        class_list=[]
        for i in trait_info:
            trait=importlib.import_module(i.replace('trait\\','').replace('.py',''))
            class_list.append(getattr(trait,trait_info[i]))
            print(getattr(trait,trait_info[i]))
        return {i.domain:i for i in class_list}
    
if __name__=='__main__':
    x=ShowPageQueue()
    a=x.task_trait_class_list()
        
#    a=['aaa','bbbbbb','ccccc']
#    for i in a:
#        if len(i)>5:
#            print(i)
#            a.insert(0,i)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
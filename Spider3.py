# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:20:30 2019

@author: dell
"""

import re
import requests
class Spider3:
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            }
    def get_html(self,url,encoding=None):
        r=requests.get(url,headers=self.headers)
        if encoding==None:
            r.encoding=r.apparent_encoding
        else:
            r.encoding=encoding
        return r.text
    
    def post_html(self,url,data,encoding=None):
        r=requests.post(url,data,headers=self.headers)
        if encoding==None:
            r.encoding=r.apparent_encoding
        else:
            r.encoding=encoding
        return r.text
    
    def get_info(self,url,encoding=None,**regex):
        text=self.get_html(url,encoding)
        for reg in regex:
            regex[reg]=re.findall(regex[reg],text,re.S)
        return regex
    
    def post_info(self,url,data,encoding=None,**regex):
        text=self.post_html(url,data,encoding)
        for reg in regex:
            regex[reg]=re.findall(regex[reg],text)
        return regex
    
if __name__ == '__main__':
    url='http://www.135zy.vip/'
    y=Spider3()
    text=y.get_html(url)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
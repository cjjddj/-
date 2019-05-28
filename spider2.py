# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:55:25 2019

@author: dell
"""

import re
import requests

class Spider:
    
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    
    def get_html(self,url,encoding=None):
        r=requests.get(url,headers=self.headers)
        if encoding==None:
            r.encoding=r.apparent_encoding 
        else:
            r.encoding=encoding 
        return r.text
    
    def post_html(self,url,data,encoding=None):
        r=requests.post(url,headers=self.headers,data=data)
        if encoding == None:
            r.encoding=r.apparent_encoding
        else:
            r.encoding=encoding
        return r.text
        
    def get_info(self,url,encoding=None,**regex):
        text=self.get_html(url,encoding=encoding)
        print(regex)
        for reg in regex:
            regex[reg]=re.findall(regex[reg],text)
        return regex
    
    def get_re_page(self,url,regex,encoding=None):
        text=self.get_html(url,encoding=encoding)
        page=re.findall(regex,text)
        print(page)
        return page
    
    
    def post_info(self,url,data,encoding=None,**regex):
        text=self.post_html(url,data)
        print(regex)
        for reg in regex:
            print(regex[reg])
            regex[reg]=re.findall(regex[reg],text)
        return regex

#if __name__ == "__main__":
#    
#    url='https://www.subo8988.com/?m=vod-detail-id-19246.html'
#    
#    x=Spider()
#    
#    info=x.get_info(url,jian_jie='<div class="vodplayinfo">(.*?)</div>')
#            
            
            
            
            
            
            
            
            
            
        
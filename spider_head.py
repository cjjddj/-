# -*- coding: utf-8 -*-
"""
111111111111111
Created on Mon May 27 15:10:23 2019

@author: 10946
"""
import re

import requests

from retry import retry

class Spider:
    
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
            }
    @retry(tries = 3, delay = 3)
    def get_html(self, url, encoding = None) :
        
        r = requests.get(url, headers = self.headers)
        
        if encoding == None:
            
            r.encoding = r.apparent_encoding
            
        else:
            
            r.encoding = encoding
        
        return r.text
        
    @retry(tries = 3, delay = 3)
    def post_html(self, url, data, encoding = None) :
        
        r = requests.post(url, headers = self.headers, data = data)
        
        if encoding == None:
            
            r.encoding = r.apparent_encoding
            
        else:
            
            r.encoding = encoding
        
        return r.text
        
    def get_info(self, url, encoding = None, **regex):
        
        html = self.get_html(url,encoding)
        
        for reg in regex:
            
            regex[reg] = re.findall(regex[reg], html)
        
        return regex
        

    def post_info(self, url, data, encoding = None, **regex):
        
        html = self.post_html(url,data,encoding)
        
        for reg in regex:
            
            regex[reg] = re.findall(regex[reg], html)
        
        return regex
    
if __name__ == '__main__':
    
    url = 'https://www.subo8988.com'
    
    x = Spider()
    
    ls = x.get_info(url, jian_jie = '<div class="pages" style="margin-bottom:10px;">共.*?条数据&nbsp;当前:.*?/(.*?)页&nbsp;<em>')
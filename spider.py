# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:18:44 2019

@author: Administrator
"""

import re

import requests

class Spider:
    
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    
    def get_html(self, url, encoding = None):
        
        r = requests.get(url, headers = self.headers)
        
        if encoding == None:
        
            r.encoding= r.apparent_encoding
        
        else:
            
            r.encoding = encoding
            
        return r.text
    
    def post_html(self, url, data, encoding = None):
        
        r = requests.post(url, headers = self.headers, data = data)
        
        if encoding == None:
        
            r.encoding= r.apparent_encoding
        
        else:
            
            r.encoding = encoding
            
        return r.text
    
    def get_info(self, url, encoding = None, **regex):#位置参数要在关键字参数之前
        
        '''
        
        {'name':'.*?', 'year':''}
        
        '''
        
        html = self.get_html(url)
        
        for reg in regex:
            
            regex[reg] = re.findall(regex[reg], html)
            
        
        return regex
    
    def post_info(self, url, data, encoding = None, **regex):
        
        
        html = self.post_html(url, data, encoding = encoding)
        
        
        for reg in regex:
            
            regex[reg] = re.findall(regex[reg], html)
            
        
        return regex
        
        
    
    
if __name__ == '__main__':
    
    url = 'https://www.subo8988.com/?m=vod-detail-id-19246.html'
    
    x = Spider()
    
    info = x.get_info(url, jian_jie = '<div class="vodplayinfo">(.*?)</div>')
    
    
    
        
        
        
        
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
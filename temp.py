# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

import requests

from spider import Spider



class Film:
    
    ######特征函数#######
    
    def split_info(self, info_str):
        
        if '/' in info_str:#表示导演用/分割开来
            
            info_str = info_str.split('/')
            
        elif ',' in info_str:
            
            info_str = info_str.split(',')
            
        elif ' ' in info_str:
            
            info_str = info_str.split(' ')
            
        else:
            
            info_str = [info_str]
            
        return [i.strip() for i in info_str if i != '']
        
        
    
    def get_film_info(self, url, encoding = None):
        
            
        
        regex = dict(
                              
                intro = '<div class="vodplayinfo">(.*?)</div>',
                
                name = '<h2>(.*?)</h2>\s+?<span>(.*?)</span>\s+?<label>(.*?)</label>',
                
                info = '\
<li>别名：<span>(.*?)</span></li>\s+?\
<li>导演：<span>(.*?)</span></li>\s+?\
<li>主演：<span>(.*?)</span></li>\s+?\
<li>类型：<span>(.*?)</span></li>\s+?\
<li class="sm">地区：<span>(.*?)</span></li>\s+?\
<li class="sm">语言：<span>(.*?)</span></li>\s+?\
<li class="sm">上映：<span>(.*?)</span></li>\s+?\
<li class="sm">片长：<span>(.*?)</span></li>\s+?\
<li class="sm">更新：<span>(.*?)</span></li>\s+?\
<li class="sm">总播放量：<span><em id="hits">.*?</script></span></li>\s+?\
<li class="sm">今日播放量：<span>(.*?)</span></li>\s+?\
<li class="sm">总评分数：<span>(.*?)</span></li>\s+?\
<li class="sm">评分次数：<span>(.*?)</span></li>',

                show_list = 'checked="" />(.*?)</li>'



                )
        
        info = Spider().get_info(url, encoding = encoding, **regex)
        
        director = self.split_info(info['info'][0][1])
            
        actor = self.split_info(info['info'][0][2])
        
        types = self.split_info(info['info'][0][3])
        
        area = self.split_info(info['info'][0][4])
        
        language = self.split_info(info['info'][0][5])
        
        m3u8_list = [url  for url in info['show_list'] if url.endswith('.m3u8')]
        
        yun_list = [url  for url in info['show_list'] if not url.endswith('.m3u8')]
        
    
        film_info = dict(
                
                name = info['name'][0][0],
                
                name_info = info['name'][0][1],
                
                grade = info['name'][0][2],
                
                athour_name = info['info'][0][0],
                
                director = director,
                
                actor = actor,
                
                types = types,
                
                area = area,
                
                language = language,
                
                show_time = info['info'][0][6],
                
                lens = info['info'][0][7],
                
                up_date = info['info'][0][8],
                
                #plays = info['info'][0][9],
                
                day_plays = info['info'][0][9],
                
                total_score =info['info'][0][10],
                
                total_score_number = info['info'][0][11],
                
                m3u8_list = m3u8_list,
                
                yun_list = yun_list,
                
                )
        
        
        return film_info
    
    
    def film_search(self, keyword, encoding = None):
        
        post_url = 'https://www.subo8988.com/index.php?m=vod-search'
        
        data = {
                'wd': keyword,
                'submit': 'search',
                
                }
        
        regex = dict(
        
                info = '<li><span class="tt"></span><span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)</a></span> <span class="xing_vb5">(.*?)</span> <span class="xing_vb6">(.*?)</span></li>'
                )
        
        info = Spider().post_info(post_url, data, encoding, **regex)
        
        joint_url = 'https://www.subo8988.com'
        
        info = [{'url':joint_url + url, 'name':name, 'types':types, 'update_time': update_time} for url, name, types, update_time in info]
        
        return {'search_list': info, 'search_word': keyword, 'host': joint_url}
    
    
    def get_show_page_info(self,url):
        
        '''
        url:'https://www.subo8988.com/?m=vod-type-id-13.html'
        
        return:
            
            {
            
            type_name:'香港剧'
            film_list:[
                    
            
            {
                    url: 'https://www.subo8988.com/?m=vod-detail-id-25401.html'
                    name: '宝宝来了[国语版] 20集全/已完结'
                    types: '香港剧'
                    update_time:'2019-05-27'
                
            
            }
            
            ...
            
            
            
            ]
            
            
            }
        
        '''
        
        pass
    
    def get_all_show_page(self):
        
        '''
        return:获取 https://www.subo8988.com/ 网站所有 show_page_url
        
        '''
        
        pass
    
    
    
    ###########功能区#######################
    
    def save_all_film_info(self):
        
        '''
        功能：将https://www.subo8988.com/所有的电影信息保存到mysql中，
        表字段为
        
        id
        name
        url
        type
        update_tiem
        
        
        '''
        pass
    
    
    
    
        
if __name__ == '__main__':
    
    url = 'https://www.subo8988.com/?m=vod-detail-id-19246.html'
    
    x = Film()
    
    #info = x.film_search('流浪地球')
    
    
        
        



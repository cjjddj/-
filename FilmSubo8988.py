# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:53:20 2019

@author: dell
"""

from spider import Spider
class FilmSubo8988():
    
    '''
    def split_info(self,info_str) 一个用在清洗数据的方法
    def get_film_info(self,url,encoding-None) 传入一个电影链接,返回连接详情数据
    def film_search(self,keyword,encoding=None) 传入一个关键字,返回搜索结果
    def get_show_page_info(self,url) 传入一个show_page_url,返回电影详情信息
    def get_all_show_page_url(self) 获取网站所有url
    def get_all_show_page_url_yield(self) 获取网站所有的show_page_url的迭代器
    '''
    domain = 'https://www.subo8988.com/'
    
    ##处理导演字段   
    def split_info(self,info_str):
        ##导演
        if '/' in info_str:
            info_str=info_str.split('/')
        elif ',' in info_str:
            info_str=info_str.split(',')
        elif ' ' in info_str:
            info_str=info_str.split(' ')
        else:
            info_str=[info_str]
        return [i.strip() for i in info_str if i != '']
    
    
    def get_film_info(self,url,encoding=None):
        regex=dict(
                intro='<div class="vodplayinfo">(.*?)</div>',
                name='<h2>(.*?)</h2>\s+?<span>(.*?)</span>\s+?<label>(.*?)</label>',
                info='\
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
                show_list='checked="" />(.*?)</li>'
                )
      
        info = Spider().get_info(url, encoding = encoding, **regex)
        
        director = self.split_info(info['info'][0][1])
            
        actor = self.split_info(info['info'][0][2])
        
        types = self.split_info(info['info'][0][3])
        
        area = self.split_info(info['info'][0][4])
        
        language = self.split_info(info['info'][0][5])
        
        m3u8_list = [url  for url in info['show_list'] if url.endswith('.m3u8')]
        
        yun_list = [url  for url in info['show_list'] if not url.endswith('.m3u8')]
        
        film_info=dict(
                
                name=info['name'][0][0],
                
                name_info=info['name'][0][1],
                
                grade=info['name'][0][2],
                ##别名
                author_name=info['info'][0],
                director=director,
                actor=actor,
                types=types,
                area=area,
                language=language,
                show_time = info['info'][0][6],
                
                lens = info['info'][0][7],
                
                up_date = info['info'][0][8],
                
                day_plays = info['info'][0][9],
                
                total_score =info['info'][0][10],
                
                total_score_number = info['info'][0][11],
                
                m3u8_list = m3u8_list,
                
                yun_list = yun_list,
               
                )
        
        return film_info
    
    def film_search(self,keyword, encoding = None):
        post_url = 'https://www.subo8988.com/index.php?m=vod-search'
        
        data = {
                'wd': keyword,
                'submit': 'search',
                }
        regex = dict(
                    info = '<li><span class="tt"></span><span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)</a></span> <span class="xing_vb5">(.*?)</span> <span class="xing_vb6">(.*?)</span></li>'
                    )
        
        info = Spider().post_info(post_url, data, encoding, **regex)
        print(info)
        join_url='https://www.subo8988.com'
        info=[{'url':join_url+url,'name':name,'types':types,'update_time':update_time} for url, name, types, update_time in info['info']]
        return {'search_list':info, 'search_word':keyword, 'host': join_url}
    
    #网站的所有url和相关字段
    def get_page_film(self,url):
        regex = dict(
                    info = '<li><span class="tt"></span><span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)</a></span> <span class="xing_vb5">(.*?)</span> <span class="xing_vb[67]">(.*?)</span></li>'
                    )
        info=Spider().get_info(url,encoding='utf-8',**regex)['info']
        info=[dict(url=i[0],name=i[1].split('&nbsp;')[0],types=i[2],update_time=i[3]) for i in info]
        return {'film_list':info}
    
    ##获取全部url
    def get_all_show_page_url_yield(self):
        url='https://www.subo8988.com/?m=vod-index-pg-{}.html'
        for i in range(1,485):
            yield url.format(i)

if __name__ == '__main__':
    url='https://www.subo8988.com/?m=vod-index-pg-2.html'
    x=FilmSubo8988()
#    info=x.get_page_film(url)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:47:28 2019

@author: dell
"""
from Spider3 import Spider3
class Film135Zy:
    
    domain='http://www.135zy.vip'
    
    def get_all_page(self,url):
        self.url='http://www.135zy.vip/?m=vod-index-pg-{}.html'
        regex=dict(
                page='共.*?条数据&nbsp;当前:1/(.*?)页'
                )
        page=Spider3().get_info(url,**regex)
        for i in range(1,int(page['page'][0])+1):
            yield self.url.format(i)
            
    def get_all_one_urls(self,url):
        regex=dict(
                href='''<span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)</a></span><span class="xing_vb5">(.*?)</span><span class="xing_vb7">(.*?)</span>'''
                )
        one_info=Spider3().get_info(url,**regex)['href']
        one_info=[dict(href=self.domain+i[0],name=i[1].split(' ')[0],types=i[2],update_time=i[3]) for i in one_info]
        return {'one_info':one_info}
    
    def get_film_two_info(self,url,encoding=None):
        regex=dict(
            name='<h2>(.*?)</h2><span>23</span><label>(.*?)</label>',
            info='\
<li>别名：<span>(.*?)</span></li>\s+?\
<li>导演：<span>(.*?)</span></li>\s+?\
<li>主演：<span>(.*?)</span></li>\s+?\
<li>类型：<span>(.*?)</span></li>\s+?\
<li>地区：<span>(.*?)</span></li>\s+?\
<li>语言：<span>(.*?)</span></li>\s+?\
<li>上映：<span>(.*?)</span></li>\s+?\
<li>更新：<span>(.*?)</span></li>\s+?',
            infro='<strong>剧情介绍：</strong></div><div class="vodplayinfo">(.*?)</div>',
            show_list='checked="" />(.*?)</li> '
            )
        two_info=Spider3().get_info(url,encoding,**regex)
        
        return two_info
if __name__=='__main__':
    f=Film135Zy()
    urls=f.get_all_one_urls(f.domain)
    two_info2=f.get_film_two_info('http://www.135zy.vip/?m=vod-detail-id-1420.html')
#    regex=dict(
#                intro = '<strong>剧情介绍：</strong></div><div class="vodplayinfo">(.*?)</div>',
#                
#                name = '<div class="vodInfo"><div class="vodh"><h2>(.*?)</h2><span>(.*?)</span><label>(.*?)</label>',
#                
#                info = 'class="vodinfobox"><ul><li>别名：<span></span></li>\
#<li>导演：<span></span></li>\
#<li>主演：<span></span></li>\
#<li>类型：<span>动漫</span></li>\
#<li>地区：<span>大陆</span></li>\
#<li>语言：<span>国语</span></li>\
#<li>上映：<span>2019</span></li>\
#<li>更新：<span>(.*?)</span></li>',
#
#            show_list = 'checked="" />(.*?)</li>'
#            )
   
    
        
    
    
    
    
    
    
    
    
    
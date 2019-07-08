# -*- coding: utf-8 -*-
"""
@author: 贾荀淘
"""
from spider import Spider


class Film135:
    
    '''
    def get_film_info(self, url, encoding = None): 
        
        传入一个电影详情链接，清洗该链接数据
        
    def film_search(self, keyword, encoding = None):
        
        传入一个关键字，返回关键字的在网站的搜索结果
        
    def get_show_page_info(self,url):
        
        传入一个show_page_url返回所有电影信息
        
    def get_all_show_page_url(self):
        
        获取网站所有的show_page_url
        
    def get_all_show_page_url_yield(self):
        
        获取网站所有的show_page_url的迭代器
     def get_all_page(self,url):
         
         动态获取网站的页数
    
    
    '''
    
    domain = 'http://www.135zy.vip/'
    
    
    def split_info(self, info_str):#一个用在清洗数据的方法
        
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
                
                name = '<div class="vodh"><h2>(.*?)</h2><span>(.*?)</span><label>(.*?)</label></div>',
                
                info = '<li>别名：<span>(.*?)</span></li><li>导演：<span>(.*?)</span></li><li>主演：<span>(.*?)</span></li><li>类型：<span>(.*?)</span></li><li>地区：<span>(.*?)</span></li><li>语言：<span>(.*?)</span></li><li>上映：<span>(.*?)</span></li><li>更新：<span>(.*?)</span></li>',

                show_list = 'checked="" />(.*?)</li>'

                )
        
        info = Spider().get_info(url, encoding = encoding, **regex)
        
        director = self.split_info(info['info'][0][1])
            
        actor = self.split_info(info['info'][0][2])
        
        types = self.split_info(info['info'][0][3])
        
        area = self.split_info(info['info'][0][4])
        
        language = self.split_info(info['info'][0][5])
        
        m3u8_list = [url.split('$')  for url in info['show_list'] if url.endswith('.m3u8')][1:]
        
        yun_list = [url.split('$')  for url in info['show_list'] if not url.endswith('.m3u8')][:-1]
        
    
        film_info = dict(
                
                name = info['name'][0][0],
                
                start_time = info['name'][0][1],
                
                grade = info['name'][0][2],
                
                athour_name = info['info'][0][0],
                
                director = director,
                
                actor = actor,
                
                types = types,
                
                area = area,
                
                language = language,
                
                show_time = info['info'][0][6],
                
                up_date = info['info'][0][7],
                
                m3u8_list = m3u8_list,
                
                yun_list = yun_list,
                
                )
        
        
        return film_info
    
    
    def film_search(self, keyword, encoding = None):
        
        post_url='http://www.135zy.vip/index.php?m=vod-search'
        
        data = {
                'wd': keyword,
                'submit': 'search',
                }
        
        regex = dict(
                
                info = '<li><span class="tt"></span><span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)</a></span><span class="xing_vb5">(.*?)</span><span class="xing_vb6">(.*?)</span>'
                )
        
        info = Spider().post_info(post_url, data, encoding, **regex)['info']
        
        joint_url = self.domain
        
        info = [{'url':joint_url + url, 'name':name, 'types':types, 'update_time': update_time} for url, name, types, update_time in info] 
        
        return {'search_list': info, 'search_word': keyword, 'host': self.domain}
    
    
    def get_show_page_info(self,url):
        
  
        regex = dict(
                
                info = '<li><span class="tt"></span><span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)</a></span><span class="xing_vb5">(.*?)</span><span class="xing_vb[67]">(.*?)</span></li>'
                
                
                )
        
        info = Spider().get_info(url,encoding = 'utf-8',**regex)['info']
        
        joint_url = self.domain
        
        info = [{'url':joint_url + url, 'name':name, 'types':types, 'update_time': update_time} for url, name, types, update_time in info] 
        
        return {'film_list': info}
      
    
    def get_all_show_page_url(self,):
        
        '''
        return:获取 http://www.135zy.co/ 网站所有 show_page_url
        
        '''
        
        url = 'http://www.135zy.vip/?m=vod-index-pg-{}.html'
        
        
        
        self.queue = [url.format(i) for i in range(1, 433)]
        
        
        return self.queue

    
    
    def get_all_show_page_url_yield(self):

        url = 'http://www.135zy.vip/?m=vod-index-pg-{}.html'

        for i in range(1, 433):

            yield url.format(i)
    
#    def get_all_page(self,url):动态获取所有页数
#        
#        rst = Spider().get_html(url)
#        
#        ye = int(str(re.findall('<li><div class="pages" style="margin-bottom:10px;">共.*?条数据&nbsp;当前:1/(.*?)页&nbsp;<em>',rst,re.S))[2:-2])
#        
#        return ye
        
if __name__ == '__main__':
    
    url = 'http://www.135zy.vip/?m=vod-index-pg-1.html'
    
    x = Film135()
    

        



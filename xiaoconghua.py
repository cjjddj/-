# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:17:01 2019

@author: 10946
"""


from spider_head import Spider

class XiaoCongHua:
    
    data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '',
            '__EVENTVALIDATION': '',
            'UcTop1$txtKey': '',
            'btn下一页': '下一页',
            }
    
    
    def __init__(self):
        self.page = self.get_page()
        self.ls = []
    
    def split_info(self, info_str):
        if '/' in info_str:
            info_str = info_str.split('/')
        elif ',' in info_str:
            info_str = info_str.split(',')
        elif ' ' in info_str:
            info_str = info_str.split(' ')
        elif '&#183;' in info_str:
            info_str = info_str.split('&#183;')
        else:
            info_str = [info_str]
        return [i.strip() for i in info_str if i != '']
    
    
    def get_form_values(self,data):
        url = 'http://www.xiaoconghuady.com/'
        regex = dict(
                info = '\
<td style="border-bottom: solid 1px #cedcdd">\s+?\
(.*?)\s+?\
</td>\s+?\
<td style="border-bottom: solid 1px #cedcdd; color: #5492c3" align="center">\s+?\
(.*?)\s+?\
</td>\s+?\
<td style="border-bottom: solid 1px #cedcdd">\s+?\
<a id="(.*?)" href="javascript:__doPostBack(.*?)"><span style=.*?>(.*?)</span></a>\s+?\
</td>\s+?\
<td align="center" style="color: Blue; border-bottom: solid 1px #cedcdd">\s+?\
(.*?)\s+?\
</td>\s+?\
<td style="color: Green; border-bottom: solid 1px #cedcdd">\s+?\
(.*?)\s+?\
</td>'
                )

        info = Spider().post_info(url,data,**regex)['info']
        info = [{'update_time':i[0].strip(),'types':i[1].strip(),'data':i[2].strip(),'name':i[4].strip(),'downloads':i[5].strip(),'publisher':i[6].strip()} for i in info]
        return info
    
    def get_page(self):
        url = 'http://www.xiaoconghuady.com/'
        regex = dict(
                page = '<span id="txt总页码">(.*?)</span>页'
                )
        page = int(Spider().get_info(url,**regex)['page'][0])
        
        return page

    
    def get_data(self,page):
        url = 'http://www.xiaoconghuady.com/'
        regex = dict(
                
                values = '<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="(.*?)" />\s+?\
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="(.*?)" />\s+?\
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />',
                values2 = '<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />\s+?\
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />'
                )
        value = Spider().get_info(url,**regex)
        self.data['__EVENTTARGET'] = value['values'][0][0]
        self.data['__EVENTARGUMENT'] = value['values'][0][1]
        self.data['__VIEWSTATE'] = value['values'][0][2]
        self.data['__VIEWSTATEGENERATOR'] = value['values2'][0][0]
        self.data['__EVENTVALIDATION'] = value['values2'][0][1]
        self.data['txt页码'] = str(page)
        return self.data

    def post_data(self,data,param):
        url = 'http://www.xiaoconghuady.com/'
        idata = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '',
            '__EVENTVALIDATION': '',
            'UcTop1$txtKey': '',
            }
        regex = dict(
                
                values = '<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="(.*?)" />\s+?\
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="(.*?)" />\s+?\
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />',
                values2 = '<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />\s+?\
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />'
                )
        value = Spider().post_info(url,data,**regex)
        idata['__EVENTTARGET'] = param
        idata['__VIEWSTATE'] = value['values'][0][2]
        idata['__VIEWSTATEGENERATOR'] = value['values2'][0][0]
        idata['__EVENTVALIDATION'] = value['values2'][0][1]
        idata['txt页码'] = data['txt页码']
        return idata
    
    def splitinfo(self,strinfo):
        if ':' in strinfo:
            s = strinfo.split(':')[1]
        elif '：' in strinfo:
            s = strinfo.split('：')[1]
        else:
            s = strinfo
        return s
    
    def isnull(self,strinfo):
        if strinfo == []:
            s = ['','','','']
        else:
            s = strinfo[0]
        return s
    def get_film_info(self,data):
        url = 'http://www.xiaoconghuady.com/Default.aspx'
        if 'btn下一页' in data.keys():
            data.pop('btn下一页')
        regex = dict(
               name = '<span id="txtMenuTitle">(.*?)</span>', 
                
               basic_info = '<td align="right">\s+?<b>发布时间：</b>\s+?</td>\s+?<td>\s+?<span id="txt发布时间">(.*?)</span>\s+?\
</td>\s+?</tr>\s+?<tr>\s+?<td align="right">\s+?<b>下载：</b>\s+?</td>\s+?<td>\s+?<span id="txt下载">(.*?)</span>次\s+?\
</td>\s+?</tr>\s+?<tr>\s+?<td align="right">\s+?<b>发布者/联盟：</b>\s+?</td>\s+?<td>\s+?<span id="txt发布者联盟">(.*?)</span>\s+?</td>',

               info = '<[pspan]{1,} style=".*?">导演[:：](.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>.*?\
<[pspan]{1,} style=".*?">(.*?)</[pspan]{1,}>',
                another_name = '<[pspan]{1,} style=".*?">又名：(.*?)</[pspan]{1,}>',
                jian_jie = '>剧情简介.*?</p><p style=".*?">(.*?)</p>',
                baidu_wangpan = '<div>.*?<a href=".*?" style="color: #ff0000;">(.*?)</a>&nbsp;<span style="color: #333333; font-family: 微软雅黑; font-size: 14px; background-color: #ffffff;">提取码：(.*?)</span></div><div>&nbsp;</div>\
<div>.*?<a href=".*?" style="color: #ff0000;">(.*?)</a>&nbsp;<span style="color: #333333; font-family: 微软雅黑; font-size: 14px; background-color: #ffffff;">提取码：(.*?)</span></div></span><br />')
        info = Spider().post_info(url,data,**regex)
        print(info['name'])
        print(data['__EVENTTARGET'])
        if info['info'] != []: 
            director = self.split_info(self.splitinfo(info['info'][0][0]))
            screenwriter = self.split_info(self.splitinfo(info['info'][0][1]))
            actor = self.split_info(self.splitinfo(info['info'][0][2]))
            types = self.split_info(self.splitinfo(info['info'][0][3]))
            area = self.split_info(self.splitinfo(info['info'][0][4]))
            language = self.split_info(self.splitinfo(info['info'][0][5]))
            times = self.split_info(self.splitinfo(info['info'][0][6]))
            film_info = dict(
                    name = info['name'][0],
                    show_time = info['basic_info'][0][0],
                    downloads = info['basic_info'][0][1],
                    publisher = info['basic_info'][0][2],
                    director = director,
                    screenwriter = screenwriter,
                    actor = actor,
                    types = types,
                    area = area,
                    language = language,
                    times = times,
                    lenth = info['info'][0][7],
                    another_name = self.isnull(info['another_name'])[0],
                    jiejian = self.isnull(info['jian_jie'])[0],
                    baidu_1080p = self.isnull(info['baidu_wangpan'])[0],
                    baidu_1080p_key = self.isnull(info['baidu_wangpan'])[1],
                    baidu_4k = self.isnull(info['baidu_wangpan'])[2],
                    baidu_4k_key = self.isnull(info['baidu_wangpan'])[3]
                    )
        else:
            film_info = ''
        return film_info


    def start(self):
        lt = []
        data = self.get_data(3)
        info = self.get_form_values(data)
        for i in info:
            if '【软件】' in i['name'] or '【公告】' in i['name'] :
                continue
            else:
                data1 = self.post_data(data,i['data'].replace('_','$'))
                film_info = self.get_film_info(data1)
                lt.append(film_info)
        return lt

if __name__ == '__main__' :
    x = XiaoCongHua()
    lst = x.start()







#    data['__EVENTTARGET'] = '新闻DataList$ctl11$LinkButton1'.replace('_','$')
#    film = x.get_film_info(data)['info']
#    
    
    
    
    
#    headers = {
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
#            }
#    import requests 
#    session = requests.session()
#    url = 'http://www.xiaoconghuady.com/Default.aspx'
#    session.post(url,data = data,headers = headers)
#    rst = session.get('http://www.xiaoconghuady.com/XWOne.aspx',headers= headers)
#    rst = rst.text
            
    
            
            
            
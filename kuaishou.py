# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:19:59 2019

@author: lenovo
"""

import requests
import os
import jpype
import threading

#from 访问快手用户主页 import KuaiShou
#
#from ks_spider import Ks_spider
from multiprocessing.dummy import Pool

class kuaishou:
    

    def __init__(self):
        
        jarpath = os.path.join(os.path.abspath("."), "F:\\JAVA\\")

        jvmPath = r'D:\program\Java\jre1.8.0_101\bin\server\jvm.dll'
        
        jpype.startJVM(jvmPath, "-ea","-Djava.class.path=%s" % (jarpath + 'ks_sig.jar'))  
        
        self.javaClass = jpype.JClass("SingatureUtil")
    
        self.t = self.javaClass()

        self.rst2 =[]
        
        self.pcursor = None
        
        self.datalist = []
        
        self.data_info = []
        
        self.user_id = []
    
    def get_info(self):
        
        url = 'http://140.143.173.241/rest/n/feed/hot?isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=59942a6c1d534a51844dfda37e92afc3&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=23&refreshTimes=7&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=510e56b366931c4cb008c51ee44664c2'
    
        r = requests.get(url)
        
        r.encoding = r.apparent_encoding
        
        rst = r.json()['feeds']
        
        for i in rst :
            
            if  'main_mv_urls'and 'main_mv_urls_sd_h265' in i :
                caption = i['caption']  #标题
                
                commenet_count = i['comment_count'] #评论人数
                
                headurl  = i['headurls'][0]['url']  #作品图片url连接
                
                like_count = i['like_count']  #点赞人数
                
                bourl = i['main_mv_urls_sd_h265'][1]['url'] #播放地址
                
                xiaurl = i['main_mv_urls'][1]['url'] #下载地址
            
                photo_id = i['photo_id']  
                
                if 'soundTrack' in i :
                    self.soundTrack_music_url = i['soundTrack']['audioUrls'][0]['url'] #音乐链接
                    
                    soundTrack_img = i['soundTrack']['avatarUrls'][0]['url'] #图片链接
                    
                    soundTrack_id  = i['soundTrack']['id']
                    
                    soundTrack_artist  = i['soundTrack']['artist']
                    
                    soundTrack_name = i['soundTrack']['name']
                    
                    soundTrack_type = i['soundTrack']['type']
                    
                    try :
                        
                        soundTrack_user_eid =i['music']['user']['eid']                    
                    
                    except KeyError:
                        soundTrack_user_eid = " "
                
                elif 'music' in i :
                    self.soundTrack_music_url = i['music']['audioUrls'][0]['url'] #音乐链接
                    
                    soundTrack_img = i['music']['avatarUrls'][0]['url'] #图片链接
                    
                    soundTrack_id  = i['music']['id']
                    
                    soundTrack_artist  = i['music']['artist']
                    
                    soundTrack_name = i['music']['name']
                    
                    soundTrack_type = i['music']['type']
                    
                    try :
                        
                        soundTrack_user_eid =i['music']['user']['eid']
            
                    except KeyError:
                        
                        soundTrack_user_eid = " "
                
                try :
                    
                    kwaiId  =i['kwaiId'] 
                    
                except KeyError:
                    
                    kwaiId='此账号无快手id'
                
                user_headurl = i['headurls'][0]['url']  #下载
                
                view_headurl = i['headurls'][1]['url']  #查看头部url
            
                user_id = i['user_id'] 
                
                user_name = i['user_name'] 
                
                user_sex = i['user_name'] 
                
                if 'F' in user_sex:
                    
                    user_sex = '女'
                    
                elif 'M' in user_sex :
                    
                    user_sex = '男'
                
                else :
                    
                    user_sex = ''
                    
                time = i['time'] #更新时间 
                
                timestamp = i['timestamp']
                
                user_type = i['type']
                    
                view_count = i['view_count']  #播放人数
                
                
                data = {'caption':caption,'commenet_count':commenet_count,'headurl':headurl,'like_count':like_count,\
                        'bourl':bourl,'xiaurl':xiaurl,'photo_id':photo_id,'soundTrack_music_url':self.soundTrack_music_url,\
                        'soundTrack_img':soundTrack_img,'soundTrack_id':soundTrack_id,'soundTrack_artist':soundTrack_artist,'soundTrack_name':soundTrack_name,\
                        'soundTrack_type':soundTrack_type,'soundTrack_user_eid':soundTrack_user_eid,'user_headurl':user_headurl,\
                        'view_headurl':view_headurl,'kwaiId':kwaiId,\
                        'user_id':user_id,'user_name':user_name,'user_sex':user_sex,'time':time,\
                        'timestamp':timestamp,'user_type':user_type,'view_count':view_count
                        }
                
                if data not in self.datalist:
                    
                     self.datalist.append(data)
            else :
                
#                with open('快手图片视频.txt') as f:
#                    f.read(i)
                
                print('此视频为图片视频')
                
    
    def java(self,srcstr):
                  
        sig = self.t.run(srcstr)
      
        return sig
    
    def get_zuoping(self,url,vurl):
        
        sig = self.java(vurl)
        
        v_url = url+vurl+'&sig='+sig.lower()
        
        r = requests.get(v_url)
        
        r.encoding = r.apparent_encoding
        
        rst = r.json()
        
        self.rst2.append(rst['feeds'])

#        data =self.rst2 #个人作品所有数据
            
        for i in self.rst2 :
            
            for c in range(len(i)):
                
                try:
                    
                    photo_id =i[c]['photo_id']
                
                except KeyError:
                    
                    print("无作品ID")  
                              
                zpinfo = {photo_id :i[c] }
                
                if zpinfo in self.data_info:
                    
                    continue
                  
                else:
                    
                    self.data_info.append(zpinfo)
               
                
        return rst 
    
    def zuoping(self,user_id):
     
#        user_id = 30003873
        
        url = 'http://140.143.173.241/rest/n/feed/profile2?'
        
        vurl = 'isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&token=&user_id={}&lang=zh&count=30&privacy=public&referer=ks%3A%2F%2Fprofile%2F1221978901%2F5245286204737794483%2F1_i%2F1636752117077655554_h86%2F8&client_key=3c2cd3f3&os=android'.format(user_id)
        
        rst2 = self.get_zuoping(url,vurl)
            
        self.pcursor=rst2['pcursor']
        
        print(rst2['pcursor'])
        
        return rst2
#    
        
    def dowork(self,user_id,pcursor):
        url = 'http://140.143.173.241/rest/n/feed/profile2?'
    
        vurl = 'isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&token=&user_id={}&lang=zh&count=30&privacy=public&pcursor={}&referer=ks%3A%2F%2Fprofile%2F118261131%2F5211227733411179550%2F1_i%2F1636757237963010050_h86%2F8&client_key=3c2cd3f3&os=android'.format(user_id,pcursor)           
        
        try:
            rst =self.get_zuoping(url,vurl)
            
            self.pcursor = rst['pcursor'] 
            
            print(rst['pcursor'])
        except Exception as e:
           
            print(e.args)
    def zuopinghou(self,user_id):

        while True :
            self.dowork(user_id,self.pcursor)
                              
            if self.pcursor == 'no_more' :
                
                break 
            for i  in x.datalist:
                for c in range(len(x.data_info)):
                    if i['photo_id']  in x.data_info[c]:
                    
                        print("ok")



    
    
    def get_zuo_infoall(self):
          
        for i in range(len(x.user_id)):

            self.zuoping(x.user_id[i])
            
            self.zuopinghou(x.user_id[i])
            
            

    def view_info(self):
        
        try:
            
            x.get_info()  ##获取热门二十条视频 一直请求一直叠加
            
        except :
            
            print('失败')
        
        for i in range(len(x.datalist)): #得到最终的热门视频值
            
            x.user_id.append(x.datalist[i]['user_id'])
        
        x.get_zuo_infoall()
             
if __name__ == '__main__' :
    
    x = kuaishou()
    
    
    x.view_info()


   
        



#    for i in range(5):
#    
#        t = threading.Thread(target=x.get_zuo_infoall)
#    
#        t.start()
#        
#        t.join()

#for i  in x.datalist:
#    for c in range(len(x.data_info)):
#        if i['photo_id']  in x.data_info[c]:
#        
#            print("ok")


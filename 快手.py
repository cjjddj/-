# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:32:58 2019

@author: dell
"""
import requests
import os
import jpype

from 访问快手用户主页 import KuaiShou
kuaishou=KuaiShou()
print(kuaishou.__class__)
#def jiemi(urlParams):
#    """
#    基本的开发流程如下：
#    ①、使用jpype开启jvm
#    ②、加载java类
#    ③、调用java方法
#    ④、关闭jvm（不是真正意义上的关闭，卸载之前加载的类）
#    """
#    # 获取jvm.dll 的文件路径
#    #jvmPath = jpype.getDefaultJVMPath()
#
#    # 加载刚才打包的jar文件
#    jarpath=os.path.join(os.path.abspath('.'),"D:\\program\\workspace2\\testSolr\\commons-lang3-3.8.jar")
#
#    jarpath2=os.path.join(os.path.abspath('.'),"D:\\program\\workspace2\\testSolr\\jiemi2.jar")
#    
#    # ①、使用jpype开启虚拟机（在开启jvm之前要加载类路径）
#    jpype.startJVM("D:\\program\\java\\jdk1.8.0_101\\jre\\bin\\server\\jvm.dll","-ea","-Djava.class.path=%s;%s"%(jarpath,jarpath2))
#    # ②、加载java类（参数是java的长类名）
#    jpype.JClass("org.apache.commons.lang3.StringUtils")
#    
#    javaClass = jpype.JClass("test.SingatureUtil")
#    
#    # 实例化java对象
#    #javaInstance = javaClass()
#    #jprint = jpype.java.lang.System.out.println 
#    # ③、调用java方法，由于我写的是静态方法，直接使用类名就可以调用方法
#    #srcStr="isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=8285bb939fb45c67c865b8afb6419baf&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=104&refreshTimes=1&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android"
#    
#    srcStr=urlParams
#    
#    sign=javaClass.genSignature(javaClass.getMapFromStr(srcStr),javaClass.FANS_SALT)
#    
#    sign=sign.lower()
#    
#    #jprint(sign)
#    
#    print(sign)
#    
#    return sign
#    # ④、关闭jvm
#    jpype.shutdownJVM()
#    
#sign=jiemi('isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=8285bb939fb45c67c865b8afb6419baf&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=104&refreshTimes=1&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android')
#print(sign)
#request.get_host()获取请求地址
#request.path获取请求的path，不带参数
#request.get_full_path()获取完整参数

url='http://103.107.217.65/rest/n/feed/hot?isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=8285bb939fb45c67c865b8afb6419baf&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=107&refreshTimes=4&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=ac2716c6c7345d3bdcc8a1c8b5cdcd99'

headers={
       'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '103.107.217.65',
        'Accept-Language': 'zh-cn'
        }

resp=requests.get(url)

jso=resp.json()

params=jso['feeds']

ls={}



for i in params:
    
    caption=i['caption'] #标题

    comment_count=i['comment_count'] #评论次数
    
    down_headUrls=i['headurls'][0]['url'] #封面图片下载地址
    
    play_headUrls=i['headurls'][1]['url'] #封面播放地址
    
    like_count=i['like_count'] #点赞
    
    if 'main_mv_urls' in i.keys():
    
        down_main_mv_urls=i['main_mv_urls'][0]['url'] #视频下载地址
        
        play_main_mv_urls=i['main_mv_urls'][1]['url'] #视频播放地址 手机app两个网址都可以播放
    
    else:
    
        down_main_mv_urls=''   
    
        play_main_mv_urls=''

    photo_id=i['photo_id']

    if 'soundTrack' in i.keys():
        
        soundTrack_music_url=i['soundTrack']['audioUrls'][0]['url'] #y音乐链接
        
        soundTrack_user_avatarUrls=i['soundTrack']['avatarUrls'][0]['url'] #背景音乐歌手图片地址
        
        soundTrack_id=i['soundTrack']['id'] #音乐id
        
        soundTrack_artist=i['soundTrack']['artist'] #背景音乐歌手
        
        soundTrack_name=i['soundTrack']['name'] #音乐名字
        
        soundTrack_type=i['soundTrack']['type'] #音乐类型
        
        try:
            
            soundTrack_user_eid=i['soundTrack']['user']['eid']
            
        except KeyError:
            
            soundTrack_user_eid=''

    elif 'music' in i.keys():
        
        soundTrack_music_url=i['music']['audioUrls'][0]['url'] #y音乐链接
        
        soundTrack_user_avatarUrls=i['music']['avatarUrls'][0]['url'] #头像播放地址
        
        soundTrack_id=i['music']['id'] #音乐id
        
        soundTrack_artist=i['music']['artist'] #艺人
        
        soundTrack_name=i['music']['name'] #音乐名字
        
        soundTrack_type=i['music']['type'] #音乐类型
        
        try:
            
            soundTrack_user_eid=i['music']['user']['eid']
            
        except KeyError:
            
            soundTrack_user_eid=''
            
    user_name=i['user_name']
     
    user_sex=i['user_sex']
    
    user_id=i['user_id']
    
    if user_sex=='F':
        
        user_sex='女'
        
    elif user_sex=='M':
        
        user_sex='男'
        
    else:
        
        user_sex=''
        
    time=i['time'] #更新时间
    
    timestamp=i['timestamp'] #时间戳
    
    view_count=i['view_count'] #浏览次数

        
    videoinfo={
            'caption':caption,'comment_count':comment_count,\
            'down_headUrls':down_headUrls,'play_headUrls':play_headUrls,\
            'like_count':like_count,'down_main_mv_urls':down_main_mv_urls,\
            'play_main_mv_urls':play_main_mv_urls,'photo_id':photo_id,'soundTrack_music_urls':soundTrack_music_url,\
            'soundTrack_user_avatarUrls':soundTrack_user_avatarUrls,'soundTrack_id':soundTrack_id,\
            'soundTrack_artist':soundTrack_artist,'soundTrack_name':soundTrack_name,'soundTrack_type':soundTrack_type,\
            'soundTrack_user_eid':soundTrack_user_eid,'user_name':user_name,'user_sex':user_sex,'time':time,'timestamp':timestamp,'view_count':view_count
            }
        
       
    ls[play_main_mv_urls]=videoinfo



import copy

a=[11,12]

b=a

'''浅拷贝会随着原来的列表改变而改变'''



'''深拷贝不会随着原来的列表改变而改变'''

c=copy.deepcopy(a)

a.append(33)





































































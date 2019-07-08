# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:18:44 2019

@author: 张鹏举
"""

import re
import glob

if __name__ == '__main__':
    
    path = ''
    
else:
    
    path = 'trait\\'


def trait_info():
    
    file_list = glob.glob(path + '*.py')
    
    #print(file_list)
    
    file_list.remove(path + '__init__.py')
    file_list.remove(path + 'spider.py')
    file_list.remove(path + 'script_trait.py')

    info_dict = {}

    for i in file_list:

        regex = 'class (.*?):'

        with open(i, encoding = 'utf-8') as f:

            content = f.read()

            class_name = re.findall(regex, content)[0]

        info_dict[i] = class_name


    return info_dict

 
    
if __name__ == '__main__':


    info = trait_info()

    
    
    
    
        
        
        
        
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

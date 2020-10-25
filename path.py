# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:38:01 2020

@author: 爬上阁楼的鱼
"""


# import sys
import os

def file_name(file_dir):
    fo = open("imgs.name", "w")
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        
        for f in files:
            if f.find('py') >= 0 :
                continue
            if f.find('name') >= 0 :
                continue
            if f.find('txt') >= 0 :
                continue
            
            print(root + "\\" + f)
            fo.write(root + "\\" + f + '\n')
        
        # print(files) #当前路径下所有非目录子文件
    
    fo.close()
    

root = os.getcwd()

file_name(root)



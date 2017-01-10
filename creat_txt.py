# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:23:51 2016

@author: Administrator
"""
#在桌面创建10个txt文件
def creat_txt():
    count = 0
    while count <= 10:
        deskpath = 'C:\\Users\\Administrator\\Desktop\\'
        fullpath = deskpath + str(count) +'.txt'
        creat_file = open(fullpath,'w')
        count = count+1

creat_txt()
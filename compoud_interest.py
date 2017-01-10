# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:50:17 2016

@author: Administrator
"""

def invest(amount,rate,time):
    
    for n in range(1,time+1):
        yearn = amount*(1+rate)**n
        print ('year'+ str(n) +'='+str(yearn))
    
invest(100,0.05,8)
    

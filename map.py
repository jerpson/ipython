# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:10:40 2017

@author: Administrator
"""

L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name.capitalize()       
L2 = list(map(normalize, L1))
#map()将传入的函数依次作用到序列的每个元素
print(L2)

from functools import reduce
def f(x,y):
    return x*y  
def prod(L):
    return reduce(f,L)
##reduce()把一个函数作用在一个序列上，这个函数必须接收两个参数，
##    reduce把结果和序列的下一个元素做累积计算    
print (prod([3,5,7,9]))

import math
def quadratic(a, b, c):
#一元二次方程求解
    if a != 0:
        if b**2 - 4*a*c >= 0:
            x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
            x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
            return x1,x2
        else:
            return None
    if a == 0:
        x = -c/b
        return x    
print (quadratic(4, 3, 1))


L1 = ['Hello', 'World', 18, 'Apple', None]

#迭代
s=[]
for i in L1:
    if isinstance(i,str)==True:
        s.append(i)
print (s)
        
#列表生成器       
print ([i for i in L1 if isinstance(i,str) == True])
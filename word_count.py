# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:29:22 2016

@author: Administrator
"""
import string

path = 'C:\\Users\\Administrator\\Desktop\\Walden.txt'
with open(path,'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}
    
for word in sorted(counts_dict, key = lambda x: counts_dict[x],reverse=True):
    print('{}--{} times'.format(word,counts_dict[word]))
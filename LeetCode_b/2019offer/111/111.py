# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/16 10:14 PM
@Author  : ddlee
@File    : 111.py
"""

##//////////////////////////// PROBLEM STATEMENT //////////////////////////
## Write a program that reads the file phillip.txt, counts the number of //
## words in the file, and prints out the count.                          //
##/////////////////////////////////////////////////////////////////////////


import sys


import re

file_name = 'phillip.txt'

cnt = 0

ptn = re.compile('\b?(\w+)\b?')

with open(file_name, 'r') as file_obj:
    for line in file_obj:
        words = ptn.findall(line)
        # print(words)
        # input(re.split('，|。|？', words))
        # words = line.strip().split()
        num_words = len(words)
        cnt += num_words
        print(num_words, words)

print('The file ' + file_name + ' has about ' + str(cnt) + ' words.')

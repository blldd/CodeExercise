# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/16 10:44 PM
@Author  : ddlee
@File    : 222.py
"""

##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Say that a "clump" in a list is a series of 2 or more adjacent elements   //
## of the same value. Print the number of clumps in the given list.          //
##    1, 2, 2, 3, 4, 4  -> 2                                                 //
##    1, 1, 2, 1, 1  -> 2                                                    //
##    1, 1, 1, 1, 1  -> 1                                                    //
##/////////////////////////////////////////////////////////////////////////////
import sys

'''
a = input()
print a
# a = a.split(', ')
a = map(int, a)
print a
'''

a = [1, 2, 2, 3, 4, 4]
# a = [1, 1, 2, 1, 1]
# a = [1, 1, 1, 1, 1]

num_of_clumps = 0
cnt = 1
last = sys.maxsize

for i in a:
    if i == last:
        cnt += 1
        if cnt == 2:
            num_of_clumps += 1
    else:
        cnt = 1
    last = i

print num_of_clumps

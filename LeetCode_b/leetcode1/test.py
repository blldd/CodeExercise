# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/20 4:46 PM
@Author  : ddlee
@File    : test.py
"""

'''
商汤二面
'''

def process(arr, target):
    l = len(arr)
    if l < 1 or target < 1:
        return False

    left = 0
    right = 1

    tmp = sum(arr[left:right])
    while right <= l:
        if tmp < target:
            right += 1
            tmp = sum(arr[left:right])

        elif tmp == target:
            return True

        elif tmp > target:
            left += 1
            tmp = sum(arr[left:right])

    return False



arr = [23,4,5,78,1,7]
target = 82

arr = [23,2,4,6,7]
target = -6
print(process(arr, target))
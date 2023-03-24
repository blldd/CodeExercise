# -*- coding:UTF-8 -*-

"""
找到数组中第一个不重复出现的整数 python
"""

import collections


# 组中不重复的数只有一个，初始值为0，然后直接遍历数组，让每个值与初始值进行异或，得出的最终值就是要找的结果：
def findNoDupOnlyOne(data):
    single = 0
    for v in data:
        single = single ^ v
    return single


# 数组中不重复的数大于一个，则可以遍历一次数组，使用一个map记录数与数出现的次数；接着，再遍历一次map，找出次数为1的数，即为我们要找的数：
# 找到第一个不重复的数字  负数会出bug
def findNoDupMany(data):
    single = 0
    Map = {}
    for i in range(len(data)):
        if data[i] in Map:
            Map[data[i]] += 1
        else:
            Map[data[i]] = 1
    for key in Map:
        if Map[key] == 1:
            single = key
            break
    return single


# 找到第一个不重复的数字  ordereddict
def findFirstNoDupMany(data):
    single = 0
    Map = collections.OrderedDict()
    for i in range(len(data)):
        if data[i] in Map:
            Map[data[i]] += 1
        else:
            Map[data[i]] = 1
    print(Map)
    for key in Map:
        if Map[key] == 1:
            single = key
            break
    return single


# 找到第一个重复的数字
def findFirstDup(numbers, duplication):
    # write code here
    numbers_set = set()
    for i in numbers:
        if i not in numbers_set:
            numbers_set.add(i)
        else:
            duplication[0] = i
            return True
    return False


list = [2, 3, 3, 1, 0, 2, 5, 3]


def nodup(list):
    for ind, i in enumerate(list):
        tmp = list[ind + 1:]
        for ind_j, j in enumerate(tmp):
            if i == j:
                break
        if ind_j == len(tmp) - 1 and i != j:
            return i


# print(nodup(list))

data = [-10, -1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
print(findFirstNoDupMany(data))

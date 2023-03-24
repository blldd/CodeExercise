#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

file_path = 'test.txt'
count = Counter()

keep = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', ' ', '-', "'", "\""]
stop_words = ['the', 'and', 'i', 'to', 'of', 'a', 'you', 'my', 'that', 'in', 'she', 'he', 'her', 'his', 'it', 'be',
              'was', 'had', 'this', 'is']

def normalize(s):
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result

with open(file_path) as file:
    for item in file.readlines():
        count.update(Counter(normalize(item).split()))
print(count.most_common())

# 追加需求：引号内元素需要算作一个单词，如何实现？
with open(file_path) as file_1:
    tmp_list1 = []
    for line in file_1.readlines():
        tmp_list = normalize(line).split('"')
        for index in range(len(tmp_list)):
            if (index + 1) % 2 != 0:
                tmp_list_handle = tmp_list[index].strip()
                tmp_list2 = tmp_list_handle.split()
                tmp_list1.extend(tmp_list2)
            else:
                tmp_list1.extend([tmp_list[index]])
    count1 = Counter(tmp_list1)
    print(count1.most_common())

# -*- coding:UTF-8 -*-

# 写一个文本统计的脚本：计算并打印有关文本文件的统计数据，包括文件里包含多少个字符、行、单词数，以及前10个出现次数最多的单词按顺序排列
import time
from collections import Counter

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

def deal_quotation(s):
    tmp_list1 = []
    tmp_list = s.split('"')
    for index in range(len(tmp_list)):
        if (index + 1) % 2 != 0:
            tmp_list_handle = tmp_list[index].strip()
            tmp_list2 = tmp_list_handle.split()
            tmp_list1.extend(tmp_list2)
        else:
            tmp_list1.extend([tmp_list[index]])
    result = ' '.join(tmp_list1)
    return result

def make_dict(s):
    words = normalize(s).split()
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d


def file_status(f):
    c = open(f).read()
    ''' 采用每次读取一行的方式
    fopen=open(f)
    c=''
    for line in fopen:
        c+=line
    '''
    print(f, 'status:')
    print('长度：', len(c))
    print('行数：', c.count('\n') + 1)
    print('单词数：', len(normalize(c).split()))
    d = make_dict(c)
    print('单词数：', sum(d[w] for w in d))
    print('不同单词数：', len([w for w in d]))
    print('单词平均长度：', sum(len(w) for w in d) / sum(d[w] for w in d))
    print('只出现过一次的单词总数：', len([d[w] for w in d if d[w] == 1]))
    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()
    print('前10名出现次数最多的单词和次数是：')
    i = 1
    for count, word in lst[:10]:
        print('%4d.%4d %s' % (i, count, word))
        i += 1
    print('前10名出现次数最多的单词和次数是(去掉功能词后)：')
    j = 1
    for count, word in lst[:]:
        if word not in stop_words and j < 11:
            print('%4d.%4d %s' % (j, count, word))
            j += 1


start_time = time.time()
file_status('test.txt')
end_time = time.time()
print('总时间：', str(end_time - start_time))

# counter = Counter()
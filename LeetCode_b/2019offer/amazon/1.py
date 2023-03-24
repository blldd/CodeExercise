# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/22 1:23 PM
@Author  : ddlee
@File    : 1.py
"""


def peak_interval(busy_list, interval):
    _max = max(map(max, busy_list))
    arr = [0 for i in range(_max + 2)]

    for busy in busy_list:
        arr[busy[0]] += 1
        arr[busy[1] + 1] += -1
    for i in range(1, _max + 2):
        arr[i] += arr[i - 1]
    print(arr)

    maxx = max(arr)
    dictt = {}
    cnt = 0
    flag = False
    start = -1
    for i, num in enumerate(arr):
        if num == maxx:
            if not flag:
                flag = True
                start = i
            cnt += 1

        else:
            if flag:
                dictt[start] = cnt
            flag = False
            cnt = 0
    dictt = sorted(dictt.items(), key=lambda x: x[1], reverse=True)
    return [dictt[0][0], dictt[0][0] + min(dictt[0][1], interval) - 1]


if __name__ == '__main__':
    busy_list = [[1, 5], [3, 9], [2, 10], [7, 10], [10, 14]]
    interval = 5
    print(peak_interval(busy_list, interval))

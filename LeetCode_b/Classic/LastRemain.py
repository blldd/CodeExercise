# -*- coding:UTF-8 -*-

"""
Josephuse环
n个人，编号0 到 n-1，每走step步移除一个人，最后剩的编号是？

method-1: 用环去模拟
method-2:分析规律  计算（有公式）
"""


def last_remain(length, step):
    if length < 1 or step < 1:
        return -1
    nums = [i for i in range(length)]
    step_cnt = 0
    remain_cnt = length
    i = -1
    while remain_cnt > 0:
        i += 1
        if i >= length:
            i = 0
        if nums[i] == -1:
            continue
        step_cnt += 1
        if step_cnt == step:
            nums[i] = -1
            step_cnt = 0
            remain_cnt -= 1
    return i

# 公式版本
def last_remain_2(length, step):
    if length < 1 or step < 1:
        return -1
    last = 0
    for i in range(2, length + 1):
        last = (last + step) % i
    return last


if __name__ == '__main__':
    for i in range(1,50):
        print(last_remain(i, 3), last_remain_2(i, 3))

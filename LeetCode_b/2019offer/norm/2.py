# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys
import math


def NB_train(train_datas, labels):
    n = len(train_datas)
    m = len(train_datas[0])

    pOut = sum(labels) / n
    p0nums = [0.0 for i in range(m)]
    p1nums = [0.0 for i in range(m)]
    p0denom = 0.0
    p1denom = 0.0
    for i in range(n):
        if labels[i] == 1:
            for j in range(m):
                p1nums[j] += train_datas[i][j]
            p1denom += sum(train_datas[i])
        else:
            for j in range(m):
                p0nums[j] += train_datas[i][j]
            p0denom += sum(train_datas[i])
    # p1vect = [math.log(i / p1denom) for i in p1nums]
    # p0vect = [math.log(i / p0denom) for i in p0nums]
    p1vect = [i / p1denom for i in p1nums]
    p0vect = [i / p0denom for i in p0nums]
    return p0vect, p1vect, pOut


def NB_predict(test_datas, p0vect, p1vect, pOut):
    n = len(test_datas)
    m = len(test_datas[0])

    ans = []
    for i in range(n):
        p1 = 0.0
        for j in range(m):
            p1 += test_datas[i][j] * p1vect[j]
        p1 += math.log(pOut)

        p0 = 0.0
        for j in range(m):
            p0 += test_datas[i][j] * p0vect[j]
        p0 += math.log(1.0 - pOut)

        if p1 > p0:
            ans.append(1)
        else:
            ans.append(0)
    return ans


if __name__ == "__main__":
    M = int(sys.stdin.readline().strip())

    train_datas = []
    for i in range(M):
        line = sys.stdin.readline().strip()
        train_data = list(map(int, line.split()))
        train_datas.append(train_data)

    labels = list(list(zip(*train_datas))[-1])

    train_datas = list(map(list, list(zip(*list(zip(*train_datas))[:-1]))))

    test_datas = []
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        line = sys.stdin.readline().strip()
        test_data = list(map(int, line.split()))
        test_datas.append(test_data)

    p0vect, p1vect, pOut = NB_train(train_datas, labels)
    ans = NB_predict(test_datas, p0vect, p1vect, pOut)
    ans = map(str, ans)
    print(" ".join(ans))

"""
14
1 1 1 0 1
1 1 1 1 1
2 1 1 0 0
3 2 1 0 0
3 3 0 0 0
3 3 0 1 1
2 3 0 1 0
1 2 1 0 1
1 3 0 0 0
3 2 0 0 0
1 2 0 0 0
2 2 1 1 0
2 1 0 0 0
3 2 1 1 1
5
1 1 0 0
1 1 1 0
1 2 1 0
2 1 0 1
2 2 1 1
"""

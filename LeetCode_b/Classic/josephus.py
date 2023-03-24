# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/5 9:33 PM
@Author  : ddlee
@File    : josephus.py
"""


def josephus_formula(n, m):
    """
    :param n: 总人数
    :param m: 每数到m去除
    :return: 返回最后一个人的下标
    """

    if n == 1:
        return 0
    else:
        return (josephus_formula(n - 1, m) + m) % n


def josephus_mimic(n, k):
    link = list(range(1, n + 1))
    ind = 0

    for loop_i in range(n - 1):
        ind = (ind + k) % len(link)
        ind -= 1

        print('Kill:', link[ind])
        del link[ind]
        if ind == -1:  # the last element of link
            ind = 0

    print('survice :', link[0])


def josephus(n, m):
    """

    Args:
        n: n people
        m: count m del

    Returns: last survive

    """
    people = list(range(1, n + 1))
    idx = 0

    last = 0
    for i in range(n):
        cnt = 0
        while cnt < m:
            if people[idx] != -1:
                cnt += 1
            if cnt == m:
                # print(people[idx])
                last = people[idx]
                people[idx] = -1
            idx = (idx + 1) % n

    return last


if __name__ == '__main__':
    n = 3
    m = 2
    ans = josephus(n, m)
    print(ans)

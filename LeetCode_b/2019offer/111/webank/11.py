# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(n, m, b, houses, cars):
    houses = list(filter(lambda x: x[-1] < b, houses))
    # print(houses)
    cars = list(filter(lambda x: x[-1] < b, cars))
    # print(cars)

    houses = sorted(houses, key=lambda x: (-x[0], x[1]))
    cars = sorted(cars, key=lambda x: -x[0])
    print(houses)
    print(cars)

    n = len(houses)
    m = len(cars)
    res = 0

    for i in range(n):
        low = 0
        high = m
        while low < high:
            mid = (low + high) >> 1
            if houses[i][-1] + cars[mid][-1] <= b:
                tmp = 10 * houses[i][0] - houses[i][1] // cars[mid][0]
                res = max(res, tmp)
                high = mid
            else:
                low = mid + 1
    return res


if __name__ == "__main__":
    n, m, b, = 3, 5, 10000000
    # area, dist,  price
    houses = [
        [100, 60000, 6000000],
        [120, 40000, 10000000],
        [200, 100000, 9000000]
    ]
    # speed, price
    cars = [
        [100, 50000],
        [200, 1000000],
        [250, 5000000],
        [240, 5000000],
        [180, 400000]
    ]

    # line1 = sys.stdin.readline().strip()
    # n, m, b = list(map(int, line1.split()))
    #
    # houses = []
    # for i in range(n):
    #     line2 = sys.stdin.readline().strip()
    #     tmp = list(map(int, line2.split()))
    #     houses.append(tmp)
    #
    # cars = []
    # for i in range(m):
    #     line3 = sys.stdin.readline().strip()
    #     tmp = list(map(int, line3.split()))
    #     cars.append(tmp)

    # 10 * area - time
    ans = process(n, m, b, houses, cars)
    print(ans)

"""
3 5 10000000
100 60000 6000000
120 40000 10000000
200 100000 9000000
100 50000
200 1000000 
250 5000000
240 5000000
180 400000
"""

# line1 = sys.stdin.readline().strip()
# n, m, b = list(map(int, line1.split()))
#
# houses = []
# for i in range(n):
#     line2 = sys.stdin.readline().strip()
#     tmp = list(map(int, line2.split()))
#     houses.append(tmp)
#
# cars = []
# for i in range(m):
#     line3 = sys.stdin.readline().strip()
#     tmp = list(map(int, line3.split()))
#     cars.append(tmp)


# -*- coding:UTF-8 -*-
import sys


def max_stock(arr):
    length = len(arr)
    if length < 2:
        return 0
    min_value = sys.maxsize
    max_diff = -1
    for i in range(length):
        min_value = min(arr[i], min_value)
        tmp = arr[i] - min_value
        max_diff = max(tmp, max_diff)
    return max_diff


if __name__ == '__main__':
    arr = [9, 11, 8, 5, 7, 12, 16, 14]
    res = max_stock(arr)
    print(res)

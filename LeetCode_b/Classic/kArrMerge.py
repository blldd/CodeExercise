# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/18 7:36 PM
@Author  : ddlee
@File    : kArrMerge.py
"""
import sys


class HeapNode:
    def __init__(self, x, i, j):
        self.val = x
        self.i = i
        self.j = j


def min_heapify(arr, parent_idx):
    l = len(arr)
    tmp = arr[parent_idx]
    child_idx = 2 * parent_idx + 1
    while child_idx < l:
        if child_idx + 1 < l and arr[child_idx + 1].val < arr[child_idx].val:
            child_idx += 1
        if tmp.val < arr[child_idx].val:
            break
        arr[parent_idx] = arr[child_idx]
        parent_idx = child_idx
        child_idx = 2 * child_idx + 1
    arr[parent_idx] = tmp


def min_heap(arr):
    l = len(arr)
    for i in range(l // 2 - 1, -1, -1):
        min_heapify(arr, i)


def k_arr_merge(k_arr):
    k = len(k_arr)
    if k <= 1:
        return k_arr

    n = len(k_arr[0])
    ans = []

    # 根据每个数组第一个构建小根堆
    knums = []
    for i in range(k):
        knums.append(HeapNode(k_arr[i][0], i, 1))
    min_heap(knums)

    for i in range(k * n):
        root = knums[0]
        ans.append(root.val)

        if root.j < n:
            root.val = k_arr[root.i][root.j]
            root.j += 1
        else:
            root.val = sys.maxsize
        knums[0] = root
        min_heapify(knums, 0)
    return ans


if __name__ == '__main__':
    k_arr = [[1, 2, 3, 7], [1, 3, 6, 9], [4, 5, 8, 11]]
    print(k_arr_merge(k_arr))

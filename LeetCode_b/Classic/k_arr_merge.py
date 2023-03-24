# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/26 10:07 PM
@Author  : ddlee
@File    : k_arr_merge.py
"""

import sys


class HeapNode:
    def __init__(self, x, i=0, j=0):
        self.value = x
        self.i = i
        self.j = j


def min_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)  # 将堆的长度单独拿出来方便
    for i in range(HeapSize // 2 - 1, -1, -1):  # 从后往前出数
        min_heapify_iter(heap, i)


def min_heapify(heap, root):
    heapsize = len(heap)
    MIN = root
    left = 2 * root + 1
    right = left + 1
    if left < heapsize and heap[MIN].value > heap[left].value:
        MIN = left
    if right < heapsize and heap[MIN].value > heap[right].value:
        MIN = right
    if MIN != root:
        heap[MIN], heap[root] = heap[root], heap[MIN]
        min_heapify(heap, MIN)


def min_heapify_iter(array, parentIndex):
    length = len(array)
    temp = array[parentIndex]
    childIndex = 2 * parentIndex + 1
    while (childIndex < length):
        if childIndex + 1 < length and array[childIndex + 1].value < array[childIndex].value:
            childIndex += 1
        if temp.value <= array[childIndex].value:
            break
        array[parentIndex] = array[childIndex]
        parentIndex = childIndex
        childIndex = 2 * childIndex + 1
    array[parentIndex] = temp


def merge_k_array(nums):
    k = len(nums)
    if k <= 1:
        return nums

    # 合并k个有序数组，每个数组长度都为k
    knums = []
    output = []
    for i in range(len(nums)):
        if len(nums[i]) > 0:
            knums.append(HeapNode(nums[i][0], i, 1))

    # k个元素初始化最小堆
    min_heap(knums)

    while knums:
        # 取堆顶，存结果
        root = knums.pop(0)
        output.append(root.value)

        # 替换堆顶
        if root.j < len(nums[root.i]):
            root.value = nums[root.i][root.j]
            root.j += 1
            knums.append(root)

        # 防止空
        if knums:
            min_heapify_iter(knums, 0)
    return output


if __name__ == '__main__':
    nums = [[1, 2, 3, 4], [1, 6, 7, 9, 11], [5, 8, 10]]
    print(merge_k_array(nums))

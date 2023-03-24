# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/25 9:12 PM
@Author  : ddlee
@File    : 23mergeKLists.py
"""

# Definition for singly-linked list.
from util_tools import build_linklist

from bisect import bisect

import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists1(self, lists):
        _sorted = sorted([(l.val, l) for l in lists if l], key=lambda x: x[0])  # 先按头节点排序
        dumb = p = ListNode(0)
        while _sorted:
            val, node = _sorted.pop(0)  # 每次取出最小节点
            p.next = node  # 插入到当前位置
            p, node = p.next, node.next
            if node:  # 所取出的节点若还有后续，把它二分插入排序好的列表
                _sorted.insert(bisect([v[0] for v in _sorted], node.val), (node.val, node))

        return dumb.next

    def mergeKLists(self, lists):
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next


if __name__ == '__main__':
    arr = [1, 4, 5, 7]
    head1 = build_linklist(arr)

    arr = [1, 2, 3, 4]
    head2 = build_linklist(arr)

    arr = [2, 6, 8, 9]
    head3 = build_linklist(arr)
    arr = [head1, head2, head3]

    root = Solution().mergeKLists(arr)
    while root:
        print(root.val)
        root = root.next

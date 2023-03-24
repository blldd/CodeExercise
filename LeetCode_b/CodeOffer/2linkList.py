# -*- coding:UTF-8 -*-
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

"""
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(listNode):
    # write code here
    l = []
    head = listNode
    while head:
        l.insert(0, head.val)
        head = head.next
    return l
    # 返回从尾部到头部的列表值序列，例如[1,2,3]


def printListFromTailToHead1(listNode):
    # write code here
    list_val = deque()  # 创建一个双边队列
    while listNode:
        list_val.appendleft(listNode.val)  # 左边插入
        listNode = listNode.next
    res = []
    for i in list_val:
        res.append(i)
    return res

def printRecursively(listNode):
    if listNode:
        if list_node.next == None:
            print(list_node.val)
        else:
            printRecursively(list_node.next)


if __name__ == '__main__':
    list_node = ListNode(1)
    list_node_2 = ListNode(2)
    list_node.next = list_node_2
    print(printListFromTailToHead(list_node))
    print(printListFromTailToHead1(list_node))
    print(printRecursively(list_node))
# -*- coding:utf-8 -*-
import numpy as np

"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop1(self, pHead):
        # write code here
        # 遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next

    """
    第一步，找环中相汇点。分别用p1，p2指向链表头部，p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。
    第二步，找环的入口。接上步，当p1==p2时，p2所经过节点数为2x,p1所经过节点数为x,设环中有n个节点,p2比p1多走一圈有2x=n+x; n=x;
    可以看出p1实际走了一个环的步数，再让p2指向链表头部，p1位置不变，p1,p2每次走一步直到p1==p2; 此时p1指向环的入口。
    """
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        pLeft = pHead
        pRight = pHead
        while pRight and pRight.next:
            pLeft = pLeft.next
            pRight = pRight.next.next
            if pLeft.val == pRight.val:
                pRight = pHead
                while pLeft != pRight:
                    pLeft = pLeft.next
                    pRight = pRight.next
                if pLeft == pRight:
                    return pLeft
        return None


if __name__ == '__main__':
    mat = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    pHead = ListNode(0)

    str1 = "Hello"


    print(Solution().EntryNodeOfLoop(pHead))
    # print(dups)
    # print(arr)

# -*- coding:utf-8 -*-
import numpy as np

"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        p = pHead.next
        if p.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == p.val and p.next is not None:
                p = p.next
            if p.val != pHead.val:
                pHead = self.deleteDuplication(p)
            else:
                return None
        return pHead

    # delete dup and save once
    def deleteD(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        p = pHead.next
        if p.val != pHead.val:
            pHead.next = self.deleteD(pHead.next)
        else:
            while p.val == pHead.val and p.next is not None:
                p = p.next
            # if p.val != pHead.val:
            pHead.next = self.deleteD(p)
            # else:
            #     return None
        return pHead

    def deleteDup(self, pHead):
        # write code here
        if not pHead:
            return None
        dummy = ListNode(-1)
        dummy.next = pHead
        q = dummy
        p = pHead
        while p and p.next:
            if p.next.val != p.val:
                q.next = p
                q = p
                p = p.next
            else:
                while p.next and p.next.val == p.val:
                    p = p.next
                p = p.next
                q.next = p
        return dummy.next


if __name__ == '__main__':
    pHead = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(4)
    n6 = ListNode(5)

    pHead.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    res = Solution().deleteDup(pHead)
    while res:
        print(res.val)
        res = res.next
    # print(dups)
    # print(arr)

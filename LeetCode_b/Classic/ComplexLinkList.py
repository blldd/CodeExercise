# -*- coding:UTF-8 -*-


class RandomListNode():
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def clone(pHead):
        if pHead == None:
            return None
        # 复制节点在原节点之后
        pCur = pHead
        while (pCur != None):
            node = RandomListNode(pCur.label)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next
        # 复制random节点
        pCur = pHead
        while (pCur != None):
            if pCur.random != None:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        head = pHead.next
        cur = head
        # 将新旧链表分离
        pCur = pHead
        while (pCur != None):
            pCur.next = pCur.next.next
            if cur.next != None:
                cur.next = cur.next.next
            cur = cur.next
            pCur = pCur.next
        return head

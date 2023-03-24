# -*- coding:UTF-8 -*-
"""
链表转置，这里实在想不到一个指针的解法了，只能用两个指针，
再加上head的帮忙，p指针记录的是每次的队头元素，q指针指向下一个要插入队头的元素
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        q = head.next
        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next
        return p

    def reverseList_recur(self, head):
        if not head or not head.next:
            return head

        # 递归返回头指针
        p = self.reverseList_recur(head.next)

        # 将还没倒置的最后一个的next指向自身，不让整个序列断掉
        head.next.next = head
        head.next = None

        return p



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
        circle_cnt = 0
        while pRight and pRight.next:
            pLeft = pLeft.next
            pRight = pRight.next.next
            circle_cnt += 1
            if pLeft.val == pRight.val:
                pRight = pHead
                left_cnt = 0
                while pLeft != pRight:
                    pLeft = pLeft.next
                    pRight = pRight.next
                    left_cnt += 1
                if pLeft == pRight:
                    return pLeft, circle_cnt, left_cnt
        return None

if __name__ == '__main__':
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    # node6.next = node3
    # res, circle_cnt, left_cnt = Solution().EntryNodeOfLoop(head)

    # print(res.val, circle_cnt, left_cnt)
    # while res.next:
    #     res = res.next
    #     print(res.val)
    # p = Solution().reverseList(head)
    # while p:
    #     print(p.val)
    #     p = p.next

    p = Solution().reverseList_recur(head)
    while p:
        print(p.val)
        p = p.next


# -*- coding:UTF-8 -*-

'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        point = head

        while point:
            if point.next != None and point.next.val == val:
                p = point
                point = point.next
                while point.next != None and point.next.val == val:
                    point = point.next
                point = point.next
                p.next = point
            else:
                point = point.next

        if head != None and head.val == val:
            head = head.next

        return head


# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/24 3:47 PM
@Author  : ddlee
@File    : 148sortList.py
"""

"""
148. 排序链表

在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # recursive
    # O(nlogn) + O(logn)
    def sortList(self, head):

        if not head or not head.next:
            return head  # termination.

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.

        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

    # iterative
    # O(nlogn) + O(1)
    def sortList_iter(self, head):
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1

        dummy = ListNode(0)
        dummy.next = head

        # merge the list in different intv.
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break  # no need to merge because the `h2` is None.

                h2, i = h, size
                while i and h:
                    h, i = h.next, i - 1

                c1, c2 = size, size - i  # the `c2`: length of `h2` can be small than the `intv`.

                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size *= 2
        return dummy.next

    def bottom_to_up_sort(self, head):

        def cut(head, size):
            p = head
            size -= 1
            while size and p:
                p = p.next
                size -= 1
            if not p:
                return None

            right = p.next
            p.next = None
            return right

        def merge(left, right):
            dummy = ListNode(0)

            p = dummy
            while left and right:
                if left.val < right.val:
                    p.next = left
                    p = left
                    left = left.next
                else:
                    p.next = right
                    p = right
                    right = right.next

            p.next = left if left else right

            return dummy.next

        dummy = ListNode(0)
        dummy.next = head

        # get length
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        # bottom to up
        size = 1
        while size < length:
            tail = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = cut(left, size)

                curr = cut(right,size)

                tail.next = merge(left, right)
                while tail.next:
                    tail = tail.next

            size <<= 1

        return dummy.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(0)
    head = Solution().bottom_to_up_sort(head)

    while head:
        print(head.val)
        head = head.next

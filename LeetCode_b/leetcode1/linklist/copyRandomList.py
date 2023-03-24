# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-07

"""Example Google style docstrings.
138. 复制带随机指针的链表

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深拷贝。

示例：

输入：
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

解释：
节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。


提示：

你必须返回给定头的拷贝作为对克隆列表的引用。
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        dummy = head

        # 1. insert clone node
        while dummy:
            clone_node = Node(dummy.val, None, None)
            clone_node.next = dummy.next
            dummy.next = clone_node

            dummy = dummy.next.next

        # 2. create random link for clone node
        dummy = head
        while dummy:
            dummy.next.random = dummy.random.next if dummy.random else None
            dummy = dummy.next.next

        # 3. split
        dummy_old = head
        dummy_new = head.next
        res = head.next

        while dummy_old:
            dummy_old.next = dummy_old.next.next
            dummy_new.next = dummy_new.next.next if dummy_new.next else None
            dummy_old = dummy_old.next
            dummy_new = dummy_new.next
        return res


if __name__ == '__main__':

    head = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, None, None)
    node4 = Node(4, None, None)
    node5 = Node(5, None, None)
    node6 = Node(6, None, None)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    head.random = node4
    node2.random = node5
    node3.random = node2
    node4.random = node4
    node5.random = node3

    # print val
    res = Solution().copyRandomList(head)

    print("next val:")
    dummy = res
    while (dummy != None):
        print(dummy.val)
        dummy = dummy.next

    print("random val:")
    dummy = res
    print(dummy.val)
    while (dummy.random != None):
        print(dummy.random.val)
        dummy = dummy.next

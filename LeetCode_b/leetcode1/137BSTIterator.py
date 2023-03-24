# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/24 11:10 PM
@Author  : ddlee
@File    : 137BSTIterator.py
"""

"""
同 94

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.arr = []
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.arr.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.arr.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.arr) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


"""
class BSTIterator(object):
    def __init__(self, root):

        self.stack_tree = []
        cur = root
        while cur:
            self.stack_tree.append(cur)
            cur = cur.left

    def next(self):

        value = self.stack_tree.pop()
        cur = value.right
        while cur:
            self.stack_tree.append(cur)
            cur = cur.left
        return value.val

    def hasNext(self):

        return len(self.stack_tree) != 0
"""

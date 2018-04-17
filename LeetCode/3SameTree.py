# -*- coding:UTF-8 -*-

'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True

        return False



if __name__ == '__main__':

    a = TreeNode(1)
    b = TreeNode(2)
    print(Solution().isSameTree(a, b))


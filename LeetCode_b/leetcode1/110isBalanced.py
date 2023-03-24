# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/21 9:44 PM
@Author  : ddlee
@File    : 110isBalanced.py
"""

# Definition for a binary tree node.
from util_tools import build_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def height(root):
            if not root:
                return 0

            return max(height(root.left), height(root.right)) + 1

        le = height(root.left)
        ri = height(root.right)
        if abs(le - ri) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    root = build_tree(arr)
    print(Solution().isBalanced(root))

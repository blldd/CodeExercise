# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/24 10:38 PM
@Author  : ddlee
@File    : 94inorderTraversal.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal_recur(root.left) + [root.val] + self.inorderTraversal_recur(root.right)

    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res


if __name__ == '__main__':
    """
    input:
         1
          \
           2
          /
         3
    output:
    [1,3,2]
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))

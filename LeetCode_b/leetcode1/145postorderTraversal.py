# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/25 10:13 PM
@Author  : ddlee
@File    : 145postorderTraversal.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
上 左 右

上 右 左 reverse 左 右 上
"""


class Solution:
    def preorderTraversal(self, root):
        stack = []
        res = []
        curr = root
        while stack or curr:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
                # res.append(curr.val)
                # curr = curr.left

        return res

    def postorderTraversal(self, root):
        stack = []
        res = []
        curr = root
        while stack or curr:
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()
        return res[::-1]


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
    print(Solution().preorderTraversal(root))
    print(Solution().postorderTraversal(root))

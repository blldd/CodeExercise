# -*- coding:utf-8 -*-
import numpy as np

"""
请实现两个函数，分别用来序列化和反序列化二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = -1

    def Serialize(self, root):
        s = ""
        s = self.recursionSerialize(root, s)
        return s

    def recursionSerialize(self, root, s):
        if (root is None):
            s = '$,'
            return s
        s = str(root.val) + ','
        left = self.recursionSerialize(root.left, s)
        right = self.recursionSerialize(root.right, s)
        s += left + right
        return s

    def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '$'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root


if __name__ == '__main__':
    pHead = TreeNode(0)
    pHead.left = TreeNode(1)
    pHead.right = TreeNode(2)
    pHead.left.left = TreeNode(3)
    pHead.right.left = TreeNode(4)
    s = Solution().Serialize(pHead)
    print(s)
    Solution.Deserialize(s)
    pass

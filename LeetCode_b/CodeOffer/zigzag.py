# -*- coding:utf-8 -*-
import numpy as np

"""
请实现一个函数按照之字形打印二叉树，即
第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        from collections import deque
        res, tmp = [], []
        last = pRoot
        q = deque([pRoot])
        left_to_right = True
        while q:
            t = q.popleft()
            tmp.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if t == last:
                res.append(tmp if left_to_right else tmp[::-1])
                left_to_right = not left_to_right
                tmp = []
                if q:
                    last = q[-1]
        return res


if __name__ == '__main__':
    pHead = TreeNode(0)
    pHead.left = TreeNode(1)
    pHead.right = TreeNode(2)
    pHead.left.left = TreeNode(3)
    pHead.right.left = TreeNode(4)
    print(Solution().Print(pHead))
    pass

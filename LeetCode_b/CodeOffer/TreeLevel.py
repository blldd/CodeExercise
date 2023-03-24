# -*- coding:utf-8 -*-
import numpy as np

"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
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
        while q:
            t = q.popleft()
            tmp.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if t == last:
                res.append(tmp)
                tmp = []
                if q:
                    last = q[-1]
        return res

    def Print1(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        tmp = [pRoot]
        while tmp:
            size = len(tmp)
            row = []
            for i in tmp:
                row.append(i.val)
            res.append(row)
            for i in range(size):
                node = tmp.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return res


if __name__ == '__main__':
    pHead = TreeNode(0)
    pHead.left = TreeNode(1)
    pHead.right = TreeNode(2)
    pHead.left.left = TreeNode(3)
    pHead.right.left = TreeNode(4)
    print(Solution().Print1(pHead))
    pass

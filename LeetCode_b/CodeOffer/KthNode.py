# -*- coding:utf-8 -*-
import numpy as np

"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def KthNode(self, pRoot, k):
        # write code here
        # 第三个节点是4
        # 前序遍历5324768
        # 中序遍历2345678
        # 后序遍历2436875
        # 所以是中序遍历，左根右
        global result
        result = []
        self.midnode(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k - 1]

    def midnode(self, root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)


if __name__ == '__main__':
    pHead = TreeNode(3)
    pHead.left = TreeNode(2)
    pHead.right = TreeNode(5)
    pHead.left.left = TreeNode(1)
    pHead.right.left = TreeNode(4)
    print(Solution().KthNode(pHead, 4).val)
    pass

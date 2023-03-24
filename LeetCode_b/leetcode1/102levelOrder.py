# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/19 9:51 PM
@Author  : ddlee
@File    : 102levelOrder.py
"""

from util_tools import build_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        last = [root]
        ans = [[root.val]]
        tmp = []
        while last:
            ans_tmp = []
            for i in range(len(last)):
                node = last.pop(0)
                if node.left:
                    tmp.append(node.left)
                    ans_tmp.append(node.left.val)
                if node.right:
                    tmp.append(node.right)
                    ans_tmp.append(node.right.val)

            last = tmp
            if ans_tmp:
                ans.append(ans_tmp)
        return ans


if __name__ == '__main__':
    arr = [3, 9, 20, "", "", 15, 7]
    root = build_tree(arr)

    print(Solution().levelOrder(root))

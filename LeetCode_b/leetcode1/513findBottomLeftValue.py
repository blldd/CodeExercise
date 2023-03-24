# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/26 8:25 PM
@Author  : ddlee
@File    : 513findBottomLeftValue.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        res=[]
        arr = [root]
        cnt = 1

        while arr:
            tmp = []
            for i in range(cnt):

                curr = arr.pop(0)
                tmp.append(curr.val)
                cnt -= 1
                if curr.left:
                    arr.append(curr.left)
                    cnt+=1
                if curr.right:
                    arr.append(curr.right)
                    cnt+=1
            res.append(tmp)
        print(res)
        return res[-1][0]


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
    root.left = TreeNode(3)
    print(Solution().findBottomLeftValue(root))

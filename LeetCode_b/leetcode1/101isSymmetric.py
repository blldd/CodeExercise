# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/18 10:06 PM
@Author  : ddlee
@File    : 101isSymmetric.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])

    last = [root]
    now = arr[1:]

    while now:
        tmp = []
        for i in range(len(last)):
            node = last[i]
            if now:
                new_node = TreeNode(now.pop(0))
                node.left = new_node
                tmp.append(new_node)
            if now:
                new_node = TreeNode(now.pop(0))
                node.right = new_node
                tmp.append(new_node)
        last = tmp

    return root


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        last = [root]
        while last:
            tmp = []
            nums = []
            for i in range(len(last)):
                node = last[i]
                if node.left:
                    tmp.append(node.left)
                    nums.append(node.left.val)
                else:
                    nums.append(None)

                if node.right:
                    tmp.append(node.right)
                    nums.append(node.right.val)
                else:
                    nums.append(None)
            last = tmp
            print(nums)
            if nums != nums[::-1]:
                return False
        return True

    def isSymmetric_(self, root):
        if not root:
            return True

        def is_sym(le, ri):
            if not le and not ri:
                return True
            if not le or not ri:
                return False
            return le.val == ri.val and is_sym(le.left, ri.right) and is_sym(le.right, ri.left)

        return is_sym(root.left, root.right)

    def isSymmetric_2(self, root):
        if not root:
            return True

        def is_sym(le, ri):
            if not le and not ri:
                return True
            if not le or not ri:
                return False
            return le.val == ri.val and is_sym(le.left, ri.right) and is_sym(le.right, ri.left)

        return is_sym(root.left, root.right)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 3]

    root = build_tree(arr)
    print(Solution().isSymmetric(root))
    print(Solution().isSymmetric_(root))

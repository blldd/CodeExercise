# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/12 10:22 PM
@Author  : ddlee
@File    : 112hasPathSum.py
"""
import collections

"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \   \
        7    2   1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def hasPathSum_(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        tmp = [(root, sum - root.val)]
        while tmp:
            node, curr_sum = tmp.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True

            if node.right:
                tmp.append((node.right, curr_sum - node.right.val))
            if node.left:
                tmp.append((node.left, curr_sum - node.left.val))

        return False


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


def level_tree(root):
    if root is None:
        return []

    arr = []
    last = [root]
    while last:
        tmp = []
        for i in range(len(last)):
            node = last[i]
            arr.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        last = tmp
    return arr


# 广度优先遍历算法
def tree_level_traversal(root):
    if root is None:
        return []

    arr = []
    my_queue = collections.deque()
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.popleft()
        arr.append(node.val)
        if node.left:
            my_queue.append(node.left)
        if node.right:
            my_queue.append(node.right)
    return arr


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.left.right = TreeNode(1)

    arr = [5, 4, 8, 11, "", 13, 4, 7, 2, "", "", "", 1]

    root = build_tree(arr)
    print(level_tree(root))
    print(tree_level_traversal(root))

    # target = 22
    # print(Solution().hasPathSum(root, target))

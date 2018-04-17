# -*- coding:UTF-8 -*-

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        self.flag = False

        def dfs(node, s):
            if node is None:
                return
            s += node.val
            if node.left is None and node.right is None:
                if s == sum:
                    self.flag = True

            dfs(node.left, s)
            dfs(node.right, s)

        dfs(root, 0)

        return self.flag


if __name__ == '__main__':

    root = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    c.left = e

    print(Solution().hasPathSum(root, 3))


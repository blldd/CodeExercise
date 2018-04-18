# -*- coding:UTF-8 -*-

'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, s, res):

            if node is None:
                return

            s += str(node.val)
            if node.left is None and node.right is None:
                res.append(int(s))

            dfs(node.left, s, res)
            dfs(node.right, s, res)


        res = []
        dfs(root, "", res)
        return sum(res)


if __name__ == '__main__':
    root = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)

    root.left = a
    root.right = b
    # a.left = c
    # a.right = d
    # c.left = e

    print(Solution().sumNumbers(root))

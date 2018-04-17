# -*- coding:UTF-8 -*-

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.right), self.height(node.left)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return True

        if abs(self.height(root.left) - self.height(root.right)) <= 1:
            if self.isBalanced(root.right) and self.isBalanced(root.left):
                return True
            else:
                return False

        else:
            return False



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

    print(Solution().height(root))
    print(Solution().isBalanced(root))


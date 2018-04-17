# -*- coding:UTF-8 -*-

'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution(object):

    # def zigzag(self, res):
    #     for i in range(len(res)):
    #         if i%2:
    #             res[i] = res[i][::-1]
    #
    #     return res
    #
    #
    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #
    #     if root is None:
    #         return []
    #
    #     res = []
    #     nodes = [root]
    #     while nodes:
    #         res.append([node.val for node in nodes])
    #
    #         next_nodes = []
    #         for node in nodes:
    #             if node.left:
    #                 next_nodes.append(node.left)
    #             if node.right:
    #                 next_nodes.append(node.right)
    #
    #         nodes = next_nodes
    #
    #     print(res)
    #     res = self.zigzag(res)
    #     return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        res = []
        nodes = [root]
        level = 0

        while nodes:
            tmp = [node.val for node in nodes]
            if level % 2 == 1:
                tmp = tmp[::-1]
            res.append(tmp)

            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            nodes = next_nodes
            level += 1

        return res



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

    print(Solution().zigzagLevelOrder(root))


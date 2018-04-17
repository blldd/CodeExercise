# -*- coding:UTF-8 -*-

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, depth, ans):
            if node is None:
                return

            depth += 1
            if node.right is None and node.left is None:
                ans.append(depth)

            dfs(node.right, depth, ans)
            dfs(node.left, depth, ans)

        ans = []
        dfs(root, 0, ans)
        return max(ans) if ans != [] else 0


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

    print(Solution().maxDepth(root))


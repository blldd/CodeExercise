# -*- coding:UTF-8 -*-

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        import copy

        ans = []

        def dfs(node, visited, ans):

            if node is None:
                return

            visited = copy.deepcopy(visited)
            visited.append(node.val)
            if node.left is None and node.right is None:
                s = 0
                for x in visited:
                    s += x
                if s == sum:
                    ans.append(visited)

            dfs(node.left, visited, ans)
            dfs(node.right, visited, ans)

        dfs(root, [], ans)

        return ans


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

    print(Solution().pathSum(root, 3))


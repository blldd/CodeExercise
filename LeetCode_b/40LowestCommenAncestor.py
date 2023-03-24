# -*- coding:UTF-8 -*-

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p is None or q is None:
            return root

        # 使用dfs得到root到p, q 的路经
        def dfs(node, visited, res):
            if node is None:
                return

            path = visited + [node.val]
            if node == p or node == q:
                res.append(path)

            dfs(node.left, path, res)
            dfs(node.right, path, res)

        res = []
        dfs(root, [], res)
        # print(res)

        i = 0
        for idx in range(min(len(res[0]), len(res[1]))):
            if res[0][idx] == res[1][idx]:
                i += 1
            else:
                return res[0][i - 1]

        return res[0][i - 1]

    def findPath(self, root, target):
        stack = []
        lastVisit = None
        while stack or root:
            # for x in stack:
            # print(x.val,)
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    lastVisit = stack.pop()
                    root = None
        return stack


if __name__ == '__main__':
    root = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    c.left = e
    e.right = f

    print(Solution().lowestCommonAncestor(root, a, d))
    # for x in Solution().findPath(a, d):
    #     print(x.val)

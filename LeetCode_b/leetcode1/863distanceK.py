# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/11 10:21 AM
@Author  : ddlee
@File    : 863distanceK.py
"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def construct_graph(root):
            graph = collections.defaultdict(list)
            dq = collections.deque()
            dq.append(root)
            while dq:
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    dq.append(node.right)
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
            return graph

        def BFS(graph, target, K):
            if target not in graph or K < 0:
                return []

            visited = []
            dq = collections.deque()
            dq.append(target)
            visited.append(target)

            level_traverse = []

            cnt = 0
            while dq:
                size = len(dq)
                level = []
                for i in dq:
                    level.append(i)
                level_traverse.append(level)
                if cnt == K:
                    break
                cnt += 1

                for i in range(size):
                    node = dq.popleft()
                    next_nodes = graph[node]

                    for node in next_nodes:
                        if node not in set(visited):
                            dq.append(node)
                            visited.append(node)

            print(visited)
            print(level_traverse)
            return [] if K >= len(level_traverse) else level_traverse[K]

        # 层序遍历树 构建图
        graph = construct_graph(root)

        # 对图从target开始进行BFS
        res = BFS(graph, target.val, K)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)


    target = TreeNode(5)

    print(Solution().distanceK(root, target, 2))

# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:46 PM
@Author  : ddlee
@File    : 3.py
"""

import sys
import collections


"""
借鉴leetcode207思路
"""

def topologicalSort(values, sequen_dict, indegrees):
    print(sequen_dict)

    queue = []
    for idx, i in enumerate(indegrees):
        if i == 0:
            queue.append((idx + 1, values[idx]))
    queue = sorted(queue, key=lambda x: (x[1], x[0]), reverse=True)

    ans = []
    while queue:
        queue = sorted(queue, key=lambda x: (x[1], x[0]), reverse=True)
        node = queue.pop()
        ans.append(node[0])
        for i in sequen_dict[node[0]]:
            indegrees[i - 1] -= 1
            if indegrees[i - 1] == 0:
                queue.append((i, values[i - 1]))
    return ans


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N, M = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    sequen_dict = collections.defaultdict(list)
    indegrees = [0] * N

    for i in range(M):
        line = sys.stdin.readline().strip()
        a, b = list(map(int, line.split()))
        sequen_dict[a].append(b)

        indegrees[b - 1] += 1

    print(sequen_dict)

    res = topologicalSort(values, sequen_dict, indegrees)

    print(res)

"""
5 6
1 2 1 1 1
1 2
1 3
1 4
2 5
3 5
4 5
"""

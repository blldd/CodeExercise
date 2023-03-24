# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/24 6:55 PM
@Author  : ddlee
@File    : 0424test.py
"""

import collections
import sys

"""

4 5
1 1 2 3
2 1 3 3
3 1 4 4
4 2 3 5
5 3 4 3
4 1

"""


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths_bfs(graph, start, end):
    paths = []
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            if next_node in path:
                continue
            elif next_node == end:
                paths.append(path + [next_node])
            else:
                todo.append([next_node, path + [next_node]])
    return paths


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    M, N = line[0], line[1]

    data = [[0 for i in range(M)] for j in range(M)]
    graph = {}
    for i in range(N):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))

        if line[1] not in graph:
            graph[line[1]] = [line[2]]
        else:
            graph[line[1]].append(line[2])
        if line[2] not in graph:
            graph[line[2]] = [line[1]]
        else:
            graph[line[2]].append(line[1])
        data[line[1] - 1][line[2] - 1] = line[3]
        data[line[2] - 1][line[1] - 1] = line[3]

    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    start, end = line[0], line[1]
    if start == end:
        print(0)
    else:
        paths = find_all_paths_bfs(graph, start, end)

        print(paths)

        if not paths:
            print("NA")
        else:
            shortest = sys.maxsize
            for path in paths:
                cost = 0
                for i in range(len(path) - 1):
                    cost += data[path[i] - 1][path[i + 1] - 1]
                if len(path) > 2:
                    cost -= (len(path) - 2)
                shortest = min(shortest, cost)
            print(shortest)

"""
aabbccbbaa
aabbcccbbaa

abcba
false
"""
#
#
# def check_double_palindrome(s):
#     length = len(s)
#     if length % 2 == 1:
#         return False
#     if s[::2] != s[1::2]:
#         return False
#     if s[::-1] != s:
#         return False
#     else:
#         return s[::2]
#
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     res = []
#     while line:
#         pld = check_double_palindrome(line)
#         if pld == False:
#             res.append("false")
#         else:
#             res.append(pld)
#
#         line = sys.stdin.readline().strip()
#
#     for i in res:
#         print(i)

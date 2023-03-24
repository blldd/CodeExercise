# -*- coding:UTF-8 -*-
import collections


class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(Solution().orangesRotting(grid))

#
# import sys
#
#
# class Solution:
#     def orangesRotting(self, grid):
#         res = 0
#         rows = grid
#         for i in range(len(rows)):
#             for j in range(len(rows[0])):
#                 if rows[i][j] == 1:
#                     if not is_path(rows, i, j):
#                         res = -1
#                         break
#                         break
#                     else:
#                         step = min_dfs(rows, i, j)
#                         print(i, j, step)
#                         res = max(res, step)
#         print(res)
#
#
# def is_path(rows, i, j):
#     res = False
#     width = len(rows[0])
#     height = len(rows)
#     if i - 1 >= 0 and rows[i - 1][j] > 0:
#         return True
#     if i + 1 < height and rows[i + 1][j] > 0:
#         return True
#     if j - 1 >= 0 and rows[i][j - 1] > 0:
#         return True
#     if j + 1 < width and rows[i][j + 1] > 0:
#         return True
#     return res
#
#
# def min_dfs(rows, i, j):
#     step = 0
#     width = len(rows[0])
#     height = len(rows)
#     _queue = [[i, j, step]]
#     while _queue:
#         i, j, step = _queue.pop(0)
#         if i - 1 >= 0 and rows[i - 1][j] > 0:
#             if rows[i - 1][j] == 2:
#                 step += 1
#                 return step
#             elif rows[i - 1][j] == 1:
#                 step += 1
#                 _queue.append([i - 1, j, step])
#         if i + 1 < height and rows[i + 1][j] > 0:
#             if rows[i + 1][j] == 2:
#                 step += 1
#                 return step
#             elif rows[i + 1][j] == 1:
#                 step += 1
#                 _queue.append([i + 1, j, step])
#         if j - 1 >= 0 and rows[i][j - 1] > 0:
#             if rows[i][j - 1] == 2:
#                 step += 1
#                 return step
#             elif rows[i][j - 1] == 1:
#                 step += 1
#                 _queue.append([i, j - 1, step])
#         if j + 1 < width and rows[i][j + 1] > 0:
#             if rows[i][j + 1] == 2:
#                 step += 1
#                 return step
#             elif rows[i][j + 1] == 1:
#                 step += 1
#                 _queue.append([i, j + 1, step])
#     return step
#
#

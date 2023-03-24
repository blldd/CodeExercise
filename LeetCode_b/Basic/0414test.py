

# # -*- coding:UTF-8 -*-
#
# import sys
#
#
# def process():
#     pass
#
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     M = int(line)
#     res = []
#
#     for i in range(M):
#         ans = 0
#         line = sys.stdin.readline().strip()
#         N = int(line)
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#
#         if len(line) <= 3:
#             ans = max(line)
#         else:
#             line = sorted(line)
#             left = line[3:]
#             boat = line[:3]
#             ans += max(boat)
#             boat.pop()
#             ans += max(boat)
#             while left:
#                 boat.append(left.pop(0))
#                 ans += max(boat)
#                 boat.pop()
#                 ans += max(boat)
#             ans -= max(boat)
#         res.append(ans)
#
#     for ans in res:
#         print(ans)

# # -*- coding:UTF-8 -*-
#
# import sys
#
#
# def process():
#     pass
#
# def permute(nums):
#     if nums is None:
#         return []
#     if nums == []:
#         return [[]]
#     permutation = []
#     stack = [-1]
#     permutations = []
#     while len(stack):
#         index = stack.pop()
#         index += 1
#         while index < len(nums):
#             if nums[index] not in permutation:
#                 break
#             index += 1
#         else:
#             if len(permutation):
#                 permutation.pop()
#             continue
#
#         stack.append(index)
#         stack.append(-1)
#         permutation.append(nums[index])
#         if len(permutation) == len(nums):
#             permutations.append(list(permutation))
#     return permutations
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     N = int(line)
#     rows = []
#     for i in range(N):
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         rows.append(line)
#
#     # for i in rows:
#     #     print(i)
#     res = sys.maxsize
#     for path in permute(range(1, N)):
#         cost = 0
#         last = 0
#         for i in path:
#             cost += rows[last][i]
#             last = i
#         cost += rows[i][0]
#         res  = min(res, cost)
#     print(res)
#


# # -*- coding:UTF-8 -*-
#
# import sys
#
#
# def process():
#     pass
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
# def find_all_paths_bfs(graph, start, end):
#     todo = [[start, [start]]]
#     while 0 < len(todo):
#         (node, path) = todo.pop(0)
#         for next_node in graph[node]:
#             if next_node in path:
#                 continue
#             elif next_node == end:
#                 yield path + [next_node]
#             else:
#                 todo.append([next_node, path + [next_node]])
#
#
# if __name__ == "__main__":
#     line_cnt = 0
#     line = sys.stdin.readline().strip()
#     rows = []
#     res = 0
#     while line and line_cnt <= 10:
#         line_cnt += 1
#         line = list(map(int, line.split()))
#         rows.append(line)
#         line = sys.stdin.readline().strip()
#     # for row in rows:
#     #     print(row)
#     for i in range(len(rows)):
#         for j in range(len(rows[0])):
#             if rows[i][j] == 1:
#                 if not is_path(rows, i, j):
#                     res = -1
#                     break
#                     break
#                 else:
#                     step = min_dfs(rows, i, j)
#                     res = max(res, step)
#     print(res)

# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/23 7:57 PM
@Author  : ddlee
@File    : 0423test.py
"""
import collections
import sys

"""
3 3
1 1 1
1 1 1
1 1 1

3 3
1 1 1
1 5 1
1 1 1
"""

def change_cnt(i, j, mat):
    pass

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    N, M = line

    if N < 1 or N > 100000 or M < 1 or M > 100000:
        print("error")
    res = 0
    mat = []

    for i in range(N):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))
        mat.append(line)

    for i in range(N):
        for j in range(M):
            change_cnt(i, j, mat)
    print(res)


"""
3
1 2 3 2
2 5 2 30000
1 4 3 4

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    line = int(line)

    if line < 1 or line > 10000:
        print("error")

    _dict = collections.defaultdict(set)

    for i in range(line):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))
        x1, y1, x2, y2 = line
        if x1 == x2 and y1 == y2:
            _dict[x1].add(y1)
        elif x1 == x2:
            if y1 < y2:
                for j in range(y1, y2 + 1):
                    _dict[x1].add(j)
            else:
                for j in range(y2, y1 + 1):
                    _dict[x1].add(j)
        else:
            if x1 < x2:
                for i in range(x1, x2 + 1):
                    _dict[i].add(y1)
            else:
                for i in range(x2, x1 + 1):
                    _dict[i].add(y1)
    res = 0
    for k, v in _dict.items():
        res += len(v)
    print(res)

# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     line = int(line)
#
#     if line < 1 or line > 10000:
#         print("error")
#
#     _set = set()
#     for i in range(line):
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         x1, y1, x2, y2 = line
#         if x1 == x2 and y1 == y2:
#             _set.add(" ".join((str(x1), str(y1))))
#         elif x1 == x2:
#             if y1 < y2:
#                 for j in range(y1, y2 + 1):
#                     _set.add(" ".join((str(x1), str(j))))
#             else:
#                 for j in range(y2, y1 + 1):
#                     _set.add(" ".join((str(x1), str(j))))
#         else:
#             if x1 < x2:
#                 for i in range(x1, x2 + 1):
#                     _set.add(" ".join((str(i), str(y1))))
#             else:
#                 for i in range(x2, x1 + 1):
#                     _set.add(" ".join((str(i), str(y1))))
#     print(_set)
#     print(len(_set))

"""

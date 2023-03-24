# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-11

"""Example Google style docstrings.

864. 获取所有钥匙的最短路径

给定一个二维网格 grid。
"." 代表一个空房间， "#" 代表一堵墙， "@" 是起点，（"a", "b", ...）代表钥匙，（"A", "B", ...）代表锁。

我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。
如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。

假设 K 为钥匙/锁的个数，且满足 1 <= K <= 6，字母表中的前 K 个字母在网格中都有自己对应的一个小写和一个大写字母。
换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。

返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。

示例 1：
输入：["@.a.#","###.#","b.A.B"]
输出：8

示例 2：
输入：["@..aA","..B#.","....b"]
输出：6

提示：

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
钥匙的数目范围是 [1, 6]，每个钥匙都对应一个不同的字母，正好打开一个对应的锁。
"""
import collections
import heapq


class Solution:
    # 关键点 + Dijkstra
    # 显然钥匙，锁，起点是图中的关键节点。
    # 先用深度优先搜索计算所有关键节点之间的距离，再用Dijkstra 算法找到每一种状态下的最小代价。

    def shortestPathAllKeys(self, grid) -> int:
        R, C = len(grid), len(grid[0])

        # The points of interest
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        # The distance from source to each point of interest
        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = collections.deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue  # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d + 1))
            return dist

        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        # Dijkstra
        pq = [(0, '@', 0)]
        final_dist = collections.defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d: continue
            if state == target_state: return d
            for destination, d2 in dists[place].items():
                state2 = state
                if destination.islower():  # key
                    state2 |= (1 << (ord(destination) - ord('a')))
                elif destination.isupper():  # lock
                    if not (state & (1 << (ord(destination) - ord('A')))):  # no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d + d2, destination, state2))

        return -1


if __name__ == '__main__':
    grid = ["@.a.#",
            "###.#",
            "b.A.B"]
    print(Solution().shortestPathAllKeys(grid))

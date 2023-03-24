# -*- coding:UTF-8 -*-

# Read only region start
import collections


class UserMainCode(object):
    def maxCircles(self, input1, input2, input3):
        '''
        给定连通性，和步长 求在步长限制内能返回的路径数量
        input1 : int
        input2 : int
        input3 : int步长

        Expected return type : int
        '''
        # Read only region end
        N = input1
        start = input2
        step = input3
        # 连通性
        dp = [[0 for j in range(N)] for i in range(N)]

        for i in range(N):
            for j in range(i + 1, N):
                if (j + 1) % (i + 1) == 0:
                    dp[i][j] = 1
                    dp[j][i] = 1
                else:
                    continue

        idx = start - 1
        level_traversal = self.tree_level(idx, N, dp, step)

        cnt = -1
        for level in level_traversal:
            for i in level:
                if i == idx:
                    cnt += 1
            print(level)
        return cnt

    def tree_level(self, pRoot, N, dp, step):
        # write code here
        if not pRoot:
            return []
        res = []
        tmp = collections.deque([pRoot])
        cnt = 0
        while tmp and cnt <= step:
            size = len(tmp)
            row = []
            for i in tmp:
                row.append(i)
            res.append(row)
            cnt += 1
            for j in range(size):
                node = tmp.popleft()
                for i in range(N):
                    if dp[node][i] == 1:
                        tmp.append(i)
        return res


if __name__ == "__main__":
    print(UserMainCode().maxCircles(3, 2, 4))

# -*- coding:UTF-8 -*-
import sys

"""
消消乐问题

"""

def archer(n, nums):
    """
    动态规划
    :param n:
    :param nums:
    :return:
    """
    dp = [[sys.maxsize for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
                continue
            if j - i == 1:
                dp[i][j] = 1 if nums[i] == nums[j] else 2
                break

    for i in range(n):
        for j in range(i, n):
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
            if nums[i] == nums[j] and i + 1 < j - 1:
                dp[i][j] = min((dp[i][j], dp[i + 1][j - 1]))
    for i in dp:
        print(i)
    return dp[0][n - 1]


def dfs(l, r):
    """
    动态规划
    递归形式
    :param l:
    :param r:
    :return:
    """

    if dp[l][r] != -1:
        return dp[l][r]
    if l == r:
        dp[l][r] = 1
        return dp[l][r]
    if r - l == 1:
        dp[l][r] = 1 if nums[l] == nums[r] else 2
        return dp[l][r]

    ans = sys.maxsize
    for k in range(l, r):
        ans = min(ans, dfs(l, k) + dfs(k + 1, r))
    if nums[l] == nums[r]:
        ans = min(ans, dfs(l + 1, r - 1))
    dp[l][r] = ans
    return dp[l][r]


if __name__ == '__main__':
    """
    问题描述：
    打气球，一下 能 连续打爆一串回文串，或者打爆一个
    求打爆所有的最少需要几次？
    """
    n = 4
    nums = [1, 4, 3, 1]
    dp = [[-1 for j in range(n)] for i in range(n)]
    print(dfs(0, n - 1))
    for i in dp:
        print(i)

    print("--" * 10)
    print(archer(n, nums))

# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/22 10:41 PM
@Author  : ddlee
@File    : 967numsSameConsecDiff.py
"""

"""
967. 连续差相同的数字

返回所有长度为 N 且满足其每两个连续位上的数字之间的差的绝对值为 K 的非负整数。
请注意，除了数字 0 本身之外，答案中的每个数字都不能有前导零。例如，01 因为有一个前导零，所以是无效的；但 0 是有效的。
你可以按任何顺序返回答案。

示例 1：
输入：N = 3, K = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。

示例 2：
输入：N = 2, K = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
"""


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        dp = set(range(10))

        for i in range(1, N):
            prev_dp = dp
            dp = set()
            for num in prev_dp:
                if num == 0:
                    continue
                remainder = num % 10
                if remainder >= K:
                    dp.add(num * 10 + remainder - K)
                if remainder + K <= 9:
                    dp.add(num * 10 + remainder + K)
        return sorted(list(dp))


if __name__ == '__main__':
    N = 3
    K = 7
    print(Solution().numsSameConsecDiff(N, K))

"""
一只股票的每日收盘价存在一个数组中，现在你选择一天买入，随后选择一天卖出，不考虑时间价值，设计算法求解可能得到的最高收益。
"""


class Solution(object):
    def maxProfit(self, prices):
        maxCur = maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur += (prices[i] - prices[i - 1])
            maxCur = max(0, maxCur)
            maxSoFar = max(maxSoFar, maxCur)
        return maxSoFar

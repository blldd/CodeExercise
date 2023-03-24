# -*- coding:UTF-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''


# 状态转移
# dp[i]表示到i位置, 所取得的最大利润
# dp[i] = dp[i-1], dp[i] - 1..i-1 最小者
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0

        dp = [None] * len(prices)
        dp[0] = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)

            if prices[i] < min_price:
                min_price = prices[i]

        return dp[-1]


if __name__ == '__main__':
    # print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))

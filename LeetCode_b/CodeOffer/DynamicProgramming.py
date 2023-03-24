# -*- coding:UTF-8 -*-

class Solution(object):
    def maxProductCuttingSolution(self, len):
        if len < 2:
            return 0
        if len == 2:
            return 1
        if len == 3:
            return 2
        products = [None for i in range(len + 1)]
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        max = 0
        for i in range(4, len + 1):
            for j in range(1, (i / 2) + 1):
                product = products[j] * products[i - j]
                if max < product:
                    max = product
                products[i] = max
        max = products[len]
        return max

    def maxProduct(self, len):
        if len < 2:
            return 0
        if len == 2:
            return 1
        if len == 3:
            return 2
        times3 = len / 3
        if len - times3 == 1:
            times3 -= 1
        times2 = (len - times3*3)/2
        return pow(3, times3) * pow(2, times2)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]

if __name__ == '__main__':
    print(Solution().maxProduct(5))
    print(Solution().rob([3,7,1,2,9,10]))

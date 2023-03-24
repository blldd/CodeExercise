import copy
from math import ceil
import numpy as np

class Solution(object):

    def canPartition_dp_2d(self, nums):
        """
        划分成两个和相等的子数组
        转化成 给定数组 和 target 求是否存在子数组能组合成target
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if not nums or l == 0:
            return True

        _sum = sum(nums)
        if _sum & 1 != 0:
            return False

        target = _sum >> 1
        dp = [[0 for _ in range(target + 1)] for _ in range(l)]
        if nums[0] <= target:
            dp[0][nums[0]] = 1

        for i in range(1, l):
            for j in range(target + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in dp:
            print(i)
        return dp[-1][-1] == 1

    def canPartition_dp_1d(self, nums):
        """
        划分成两个和相等的子数组
        转化成 给定数组 和 target 求是否存在子数组能组合成target
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if not nums or l == 0:
            return True

        _sum = sum(nums)
        if _sum & 1 != 0:
            return False

        target = _sum >> 1
        dp = [0 for _ in range(target + 1)]
        if nums[0] <= target:
            dp[nums[0]] = 1

        for i in range(1, l):
            for j in range(target, -1, -1):  # !!!
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
                else:
                    break
            print(dp)

        return dp[-1] == 1

    def canPartition(self, nums):
        """
        划分成两个和相等的子数组
        转化成 给定数组 和 target 求是否存在子数组能组合成target
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return True

        _sum = sum(nums)
        if _sum & 1 != 0:
            return False

        half_sum = _sum >> 1
        dp = [0] * (half_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(half_sum, num - 1, -1):
                dp[j] = 1 if dp[j] or dp[j - num] else 0
            print(dp)

        return dp[half_sum] == 1

    # 最小差划分
    def min_diff_partition(self, nums):
        """
        划分成两个和相等的子数组
        转化成 给定数组 和 target 求是否存在子数组能组合成target
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if not nums or l == 0:
            return True

        _sum = sum(nums)
        if _sum & 1 != 0:
            return False

        target = _sum >> 1
        dp = [[0] * (target + 1) for _ in range(l)]
        if nums[0] <= target:
            dp[0][nums[0]] = nums[0]

        for i in range(1, l):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in dp:
            print(i)
        return max(dp[-1])

    # 返回划分结果
    def min_diff_partition_ret(self, nums):
        """
        划分成两个和相等的子数组
        转化成 给定数组 和 target 求是否存在子数组能组合成target
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if not nums or l == 0:
            return True

        _sum = sum(nums)
        if _sum & 1 != 0:
            return False

        target = _sum >> 1
        dp = [[0] * (target + 1) for _ in range(l)]
        if nums[0] <= target:
            dp[0][nums[0]] = nums[0]

        flag = [[0 for _ in range(target + 1)] for _ in range(l)]
        flag[0][nums[0]] = -1

        for i in range(1, l):
            for j in range(target + 1):
                if j >= nums[i]:
                    if dp[i - 1][j] > dp[i - 1][j - nums[i]] + nums[i]:
                        dp[i][j] = dp[i - 1][j]
                        flag[i][j] = j
                    else:
                        dp[i][j] = dp[i - 1][j - nums[i]] + nums[i]
                        flag[i][j] = -1
                else:
                    dp[i][j] = dp[i - 1][j]
                    flag[i][j] = j

        # for i in dp:
        #     print(i)
        # print()
        # for i in flag:
        #     print(i)

        # 同 64
        path = []
        i, j = l - 1, np.argsort(dp[-1])[-1]
        while i >= 0 and j >= 0:
            if flag[i][j] == -1:
                path.append(nums[i])
                j -= nums[i]
                i -= 1
            else:
                i -= 1

        # print(path)
        return max(dp[-1])


if __name__ == '__main__':
    nums = [5, 2, 3, 5, 5]
    nums = [1, 5, 11, 5]
    nums = [1, 2, 5]
    nums = [2, 2, 3, 5]

    # print(Solution().canPartition_dp_2d(nums))
    # print(Solution().canPartition_dp_1d(nums))
    # print(Solution().canPartition(nums))
    # print(Solution().min_diff_partition(nums))
    print(Solution().min_diff_partition_ret(nums))

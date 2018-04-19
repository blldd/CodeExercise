# -*- coding:UTF-8 -*-

'''

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.'''
class Solution(object):

    # 二分查找
    # As to NLogN solution, logN immediately reminds you of binary search.
    # In this case, you cannot sort as the current order actually matters.
    # How does one get an ordered array then?
    # Since all elements are positive, the cumulative sum must be strictly increasing.
    # Then, a subarray sum can expressed as the difference between two cumulative sum.
    # Hence, given a start index for the cumulative sum array, the other end index can be searched using binary search.
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        minLen = len(nums) + 1
        for i in range(len(sums)):
            end = self.binarySearch(i + 1, len(sums) - 1, sums[i] + s, sums)
            if end == len(sums):
                break
            if end - i < minLen:
                minLen = end - i

        return minLen if minLen != len(nums) + 1 else 0

    def binarySearch(self, low, high, key, sums):
        while low <= high:
            mid = int((low + high) / 2)
            if sums[mid] >= key:
                high = mid - 1
            else:
                low = mid + 1

        return low


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
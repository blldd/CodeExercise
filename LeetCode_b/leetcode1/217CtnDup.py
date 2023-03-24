"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Subscribe to see which companies asked this question.
"""
"""利用hash table，别忘了判断空数组的情况.其实更麻烦"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        dic = dict()
        for num in nums:
            if num in dic:
                return True
            dic[num] = 1
        return False


"""直接利用set的性质反而更简单"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
"""仍然用dict保存数组元素出现的位置，两种情况下更新"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = dict()
        for index, value in enumerate(nums):
            if value in dic and index - dic[value] <= k:
                return True
            dic[value] = index
        return False

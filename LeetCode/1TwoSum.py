# -*- coding:UTF-8 -*-

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#  采用双向指针
class Solution(object):

    # 复杂度太高了
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if nums[i] + nums[j] == target:
    #                 return [j, i]

    # # 还是慢, O(nlogn)
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     # print(list(enumerate(nums)))
    #     nums = sorted(enumerate(nums), key=lambda x: x[1])
    #     print(nums)
    #     i = 0
    #     j = len(nums) - 1
    #
    #     while i < j:
    #         if nums[i][1] + nums[j][1] > target:
    #             j -= 1
    #
    #         if nums[i][1] + nums[j][1] < target:
    #             i += 1
    #
    #         if nums[i][1] + nums[j][1] == target:
    #             return sorted([nums[i][0], nums[j][0]])


    # # hash table, 不需要排序, 对于当前nums[i], 我们查询 target - nums[i] 所在位置
    def twoSum(self, nums, target):

        dict_num_to_position = {}

        for i in range(len(nums)):
            if target - nums[i] in dict_num_to_position:
                return [dict_num_to_position[target - nums[i]], i]

            dict_num_to_position[nums[i]] = i


if __name__ == '__main__':
    nums = [3, 1, 2]
    target = 5
    print(Solution().twoSum(nums, target))


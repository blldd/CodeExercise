# -*- coding:UTF-8 -*-

'''

'''


class Solution(object):
    def isContinous(self, nums):
        # write code here
        length = len(nums)
        if nums is None and length < 1:
            return False
        nums = sorted(nums)
        # print(nums)
        numOfZero = 0
        numOfGap = 0
        for i in range(length):
            if nums[i] == 0:
                numOfZero += 1

        left = numOfZero
        right = left + 1
        while right < length:
            if nums[left] == nums[right]:
                return False
            numOfGap += nums[right] - nums[left] - 1
            left += 1
            right += 1

        if numOfZero >= numOfGap:
            return True
        else:
            return False



if __name__ == '__main__':
    nums = [1, 2, 4, 7, 0, 0]
    # nums = []
    target = "I am a student."
    tar = "abcdefg"
    matrix = ["a", "b", "c", "e", "s", "f", "c", "s", "a", "d", "e", "e"]
    path = ["b", "c", "c", "e"]
    print(Solution().isContinous(nums))
    # print(Solution().dp_probability(3, 18))

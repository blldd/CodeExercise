# -*- coding:UTF-8 -*-

'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
'''


class Solution(object):
    def findNumWithSum(self, data, length, target, num1, num2):
        if not data:
            return None
        left = 0
        right = length - 1
        while(right > left):
            tmp = data[left] + data[right]
            if(tmp == target):
                num1 = data[left]
                num2 = data[right]
                break
            elif tmp > target :
                right = right - 1
            else:
                left = left + 1

        return num1, num2


if __name__ == '__main__':
    nums = [1, 2, 4, 7, 8, 11, 13, 15]
    # nums = []
    target = 15
    print(Solution().findNumWithSum(nums, len(nums), target, 0, 0))

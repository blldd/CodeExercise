# -*- coding:UTF-8 -*-

'''
找出整型数组里除了两个数字以外，其它都出现了两次。要求时间复杂度是O(n) 空间复杂度是 O(1)
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
    nums = [1, 2, 4, 7, 11, 15]
    # nums = []
    target = 15
    print(Solution().findNumWithSum(nums, len(nums), target, 0, 0))

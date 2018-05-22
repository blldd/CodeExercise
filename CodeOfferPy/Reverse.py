# -*- coding:UTF-8 -*-

'''
找出整型数组里除了两个数字以外，其它都出现了两次。要求时间复杂度是O(n) 空间复杂度是 O(1)
'''


class Solution(object):
    def reverse(self, target):
        arr = target.split(" ")
        arr.reverse()
        return " ".join(arr)

    def leftRotate(self, target, num):
        arr = [x for x in target]
        subArr = arr[0 : num]
        subArr2 = arr[num:]
        # subArr.reverse()
        # subArr2.reverse()
        return "".join(subArr2) + "".join(subArr)



if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    # nums = []
    target = "I am a student."
    tar = "abcdefg"
    print(Solution().leftRotate(tar, 2))

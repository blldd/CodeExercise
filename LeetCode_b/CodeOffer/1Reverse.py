# -*- coding:UTF-8 -*-

'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
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
    # print(Solution.reverse(target))
    print(Solution().leftRotate(tar, 2))

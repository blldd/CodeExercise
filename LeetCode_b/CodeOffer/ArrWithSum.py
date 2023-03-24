# -*- coding:UTF-8 -*-

'''
找出整型数组里除了两个数字以外，其它都出现了两次。要求时间复杂度是O(n) 空间复杂度是 O(1)
'''


class Solution(object):
    def printContiSeq(self, small, big):
        for i in range(small, big + 1):
            print(i)
        print()

    def findContiSeq(self, target):
        if target < 3:
            return;
        small = 1
        big = 2
        tmp = small + big
        mid = (1 + target) / 2

        while small < mid:
            if tmp == target:
                print(" ".join([str(x) for x in range(small, big + 1)]))
                # self.printContiSeq(small, big)

            while tmp > target and small < mid:
                tmp = tmp - small
                small = small + 1
                if (tmp == target):
                    print(" ".join([str(x) for x in range(small, big + 1)]))
                    # self.printContiSeq(small, big)
            big = big + 1
            tmp = tmp + big


if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    # nums = []
    target = 15
    print(Solution().findContiSeq(target))

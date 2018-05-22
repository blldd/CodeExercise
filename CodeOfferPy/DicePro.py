# -*- coding:UTF-8 -*-

'''
找出整型数组里除了两个数字以外，其它都出现了两次。要求时间复杂度是O(n) 空间复杂度是 O(1)
'''


class Solution(object):
    def dp_probability(self, n, sum, dmax=6, dmin=1):
        if sum < n * dmin or sum > n * dmax:
            return 0
        dp1 = [0] * (n * dmax + 1)
        # init dp[1, :]
        for i in range(1, dmax + 1):
            dp1[i] = 1
            # i: the number of dices
        for i in range(2, n + 1):
            dp2 = [0] * (n * dmax + 1)
            # j: range of i dices
            for j in range(dmin * i, dmax * i + 1):
                # k: range of new added dice
                for k in range(dmin, dmax + 1):
                    if j > k:
                        dp2[j] += dp1[j - k]
                print(dp2)
            dp1 = dp2
        print("total = {0}, prob = {1}%".format(dp2[sum], dp2[sum] * 100 / dmax ** n))
        return dp2[sum]

    def dicePro(self, target, num):
        tmpArr1 = [0 for x in range(6 * num + 1)]

        for x in range(1, 7):
            tmpArr1[x] = 1
        flag = 0
        for i in range(2, num + 1):
            tmpArr2 = [0 for x in range(6 * num + 1)]
            for j in range(i, i * 6 + 1):
                for k in range(1, 7):
                    if j > k:
                        tmpArr2[j] += tmpArr1[j - k]
                flag = 1
            # else:
            #     for j in range(i, i * 6 + 1):
            #         for k in range(1, 7):
            #             if j > k:
            #                 tmpArr1[j] += tmpArr2[j - k]
            #     flag = 0
            tmpArr1 = tmpArr2

        print(tmpArr1)
        print(tmpArr2)
        print("total = {0}, prob = {1}%".format(tmpArr2[target], tmpArr2[target] * 100 / 6 ** num))

        return tmpArr1[target]
        # > tmpArr1[target - 1] ? tmpArr2[target - 1]: tmpArr1[target - 1]


if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    # nums = []
    target = "I am a student."
    tar = "abcdefg"
    print(Solution().dicePro(18, 3))
    # print(Solution().dp_probability(3, 18))

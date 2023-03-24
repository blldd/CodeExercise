# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 9:20 AM
@Author  : ddlee
@File    : 784letterCasePermutation.py
"""


class Solution:
    """
    给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

    示例:
    输入: S = "a1b2"
    输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
    """

    def letterCasePermutation(self, S):
        length = len(S)
        n = 2 ** length

        res = set()
        for i in range(n):
            tmp = ""
            for j in range(length):
                if ((2 ** j) & i) == 0:
                    tmp += S[j].lower()
                else:
                    tmp += S[j].upper()
            if tmp not in res:
                res.add(tmp)
        return list(res)
    #
    # def letterCasePermutation(self, S):
    #     if len(S) < 1:
    #         return []
    #     digits = set([str(i) for i in range(10)])
    #
    #     chars = ""
    #     digit_idxs = {}
    #     for idx, c in enumerate(S):
    #         if c in digits:
    #             digit_idxs[idx] = c
    #         else:
    #             chars += c
    #     # print(digit_idxs)
    #     # print(chars)
    #
    #     res = set()
    #     for i in range(2 ** len(chars)):
    #         tmp = ""
    #         for j in range(len(chars)):
    #             if ((2 ** j) & i) == 0:
    #                 tmp += chars[j].lower()
    #             else:
    #                 tmp += chars[j].upper()
    #         res.add(tmp)
    #     ans = []
    #     for s in res:
    #         arr = list(s)
    #         for item in digit_idxs.items():
    #             arr.insert(item[0], item[1])
    #         ans.append("".join(arr))
    #     return ans


if __name__ == '__main__':
    S = "a1b2"
    print(Solution().letterCasePermutation(S))

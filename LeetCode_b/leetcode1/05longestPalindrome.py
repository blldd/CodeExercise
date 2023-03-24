# -*- coding:UTF-8 -*-
class Solution:
    def longestPalindrome(self, s):
        """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
        输入: "babad"
        输出: "bab"
        :param s:
        :return:
        """
        res = ""
        max_len = 0
        # rs = s[::-1]
        length = len(s)
        for idx, i in enumerate(s):
            # 奇数
            for j in range(length - idx):
                if idx - j >= 0 and idx + j <= length and s[idx - j] == s[idx + j]:
                    if 2 * j + 1 > max_len:
                        max_len = 2 * j + 1
                        res = s[idx - j:idx + j + 1]
                else:
                    break

            # 偶数
            for j in range(length - idx - 1):
                if idx - j >= 0 and idx + j + 1 <= length and s[idx - j] == s[idx + j + 1]:
                    if 2 * (j + 1) > max_len:
                        max_len = 2 * (j + 1)
                        res = s[idx - j:idx + j + 2]
                else:
                    break
        return res


if __name__ == '__main__':
    s = "abcda"
    print(Solution().longestPalindrome(s))

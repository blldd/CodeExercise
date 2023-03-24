# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/29 10:37 PM
@Author  : ddlee
@File    : 151reverseWords.py
"""

"""
151. 翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。


示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

import re

class Solution:
    def reverseWords(self, s):
        s = s.strip()
        arr = s.split()
        print(arr)

        def remove_punctuation(text):
            r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
            pun = re.match(r, text)
            return re.sub(r, ' ', text).strip()

        res = []

        for s in arr:
            s_strip = remove_punctuation(s)
            pun = ""
            for idx, i in enumerate(s):
                if idx < len(s_strip) and i == s_strip[idx]:
                    continue
                else:
                    pun+=i
            res.append(s_strip[::-1]+pun)
        return ' '.join(res)


if __name__ == '__main__':
    s = "  hello world!  "
    print(Solution().reverseWords(s))

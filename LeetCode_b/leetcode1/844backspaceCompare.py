# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-10

"""Example Google style docstrings.
844. 比较含退格的字符串

给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []

        for ch in S:
            if ch != '#':
                stack_s.append(ch)
            else:
                if len(stack_s) > 0:
                    stack_s.pop()

        for ch in T:
            if ch != '#':
                stack_t.append(ch)
            else:
                if len(stack_t) > 0:
                    stack_t.pop()

        ls = len(stack_s)
        lt = len(stack_t)
        if ls != lt:
            return False

        for i in range(ls):
            if stack_s[i] != stack_t[i]:
                return False
        return True


if __name__ == '__main__':
    S = "a##c"
    T = "#a#c"
    print(Solution().backspaceCompare(S, T))

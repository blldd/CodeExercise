# -*- coding:UTF-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

    def longestValidParentheses(self, s):
        """
        给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度
        :type s: str
        :rtype: int
        """
        length = len(s)

        if length < 2:
            return 0
        stack = []

        for i in range(length):
            if s[i] == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                    continue
            stack.append(i)

        max_length = 0
        next_index = len(s)
        while stack:
            cur_index = stack.pop()
            cur_length = next_index - cur_index - 1
            max_length = max(max_length, cur_length)
            next_index = cur_index
        max_length = max(max_length, next_index)

        return max_length

    def longestValidParentheses_dp(self, s):
        """
        给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度

        dp数组来存放以每个index为结尾的最长有效括号子串长度
        例如：dp[3] = 2代表以index为3结尾的最长有效括号子串长度为2
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        dp = [0 for i in s]

        for i in range(1, len(s)):
            if s[i] == ")":
                left = i - 1 - dp[i - 1]
                if left >= 0 and s[left] == "(":
                    dp[i] = dp[i - 1] + 2
                    if left > 0:
                        dp[i] += dp[left - 1]
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = ")(()))"
    print(Solution().longestValidParentheses_dp(s))
    # print(Solution().isValid(s))

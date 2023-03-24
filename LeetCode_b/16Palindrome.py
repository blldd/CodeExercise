# -*- coding:UTF-8 -*-

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

'''


# 状态转移
# dp[i]表示到i位置, 所取得的最大利润
# dp[i] = dp[i-1], dp[i] - 1..i-1 最小者
class Solution(object):

    def is_alphanumeric(self, c):
        if ord(c) in range(48, 58):
            return True
        if ord(c) in range(97, 123):
            return True
        return False

    # def isPalindrome(self, s):
    #     if s == "":
    #         return True
    #
    #     s = s.lower()
    #     i = 0
    #     array = []
    #     while i < len(s):
    #         if self.is_alphanumeric(s[i]):
    #             array.append(s[i])
    #         i += 1
    #
    #     j = 0
    #     arrayLen = len(array)
    #     while j < arrayLen/2:
    #         if array[j] != array[arrayLen-1-j]:
    #             return False
    #         j += 1
    #     return True

    # perfect
    def isPalindrome(self, s):
        if s == "":
            return True

        s = s.lower()
        i = 0
        j = len(s) - 1

        while i <= j:
            if self.is_alphanumeric(s[i]):
                if self.is_alphanumeric(s[j]):
                    if s[i] != s[j]:
                        return False
                    j -= 1
                    i += 1
                else:
                    j -= 1
            else:
                i += 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

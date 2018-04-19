# -*- coding:UTF-8 -*-

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''



class Solution(object):

    def isValid2(self, s):
        stack = []

        sLen = len(s)
        if sLen == 0:
            return True
        if sLen%2:
            return False

        for i in range(sLen/2):
            stack.append(s[i])

        for i in range(sLen/2, sLen):
            c = s[i]
            if c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False

            if c == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":

                if len(stack) == 0:
                    return False
                if c == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

                if c == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

                if c == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False

        if stack == []:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isValid("]"))

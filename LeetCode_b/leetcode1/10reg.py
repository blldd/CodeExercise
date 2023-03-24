# -*- coding:UTF-8 -*-

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def helper(s, i, p, j):
            if j < -1:
                return False
            if j == -1:
                return i == -1

            if i == -1:
                if p[j] != '*':
                    return False
                return helper(s, i, p, j - 2)

            if p[j] == '*':
                if p[j - 1] == '.' or p[j - 1] == s[i]:
                    if helper(s, i - 1, p, j):
                        return True
                return helper(s, i, p, j - 2)

            if p[j] == '.' or p[j] == s[i]:
                return helper(s, i - 1, p, j - 1)

            return False

        return helper(s, len(s) - 1, p, len(p) - 1)

    def isMatch_dp(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        dp[0][0] = 1

        # init the first line
        for i in range(2, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in dp:
            print(i)
        print("--" * 10)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    elif p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]

                elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        for i in dp:
            print(i)
        print("--" * 10)
        return dp[m][n] == 1


if __name__ == '__main__':
    s = "ac"
    p = ".*"
    print(Solution().isMatch_dp(s, p))

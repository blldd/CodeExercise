# -*- coding:UTF-8 -*-

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == p
        dp = [[0 for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        dp[0][0] = 1
        for idx, char in enumerate(p):
            if char == "*":
                dp[0][idx + 1] = 1
            else:
                break
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    # tmp = []
                    # for k in range(i + 1):
                    #     tmp.append(dp[k][j - 1])
                    dp[i][j] = 1 if (dp[i - 1][j] or dp[i][j - 1]) else 0
                else:
                    dp[i][j] = 1 if (dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "?")) else 0

        for i in dp:
            print(i)
        return dp[-1][-1] == 1


    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ps, pp, match, star_idx = 0, 0, 0, -1
        while ps < len(s):
            if pp < len(p) and (p[pp] == '?' or s[ps] == p[pp]):  # advancing both pointers
                ps += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':  # found '*', only advancing pattern pointer
                star_idx = pp
                match = ps
                pp += 1
            elif star_idx != -1:  # last pattern pointer was *, advancing string pointer
                pp = star_idx + 1
                match += 1
                ps = match
            else:  # current pattern pointer is not star, last patter pointer was not *， characters do not match
                return False
        while pp < len(p) and p[pp] == '*':  # check for remaining characters in pattern
            pp += 1
        return pp == len(p)


if __name__ == '__main__':
    s = "abceb"
    p = "*a*b"
    print(Solution().isMatch2(s, p))

    # p = [[1, 1, 0, 0, 0],
    #      [0, 1, 1, 1, 0],
    #      [0, 1, 0, 1, 1],
    #      [0, 1, 1, 1, 0],
    #      [0, 1, 0, 1, 0],
    #      [0, 1, 0, 1, 1]]
    # print(p[:][1])

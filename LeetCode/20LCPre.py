# -*- coding:UTF-8 -*-

'''
Write a function to find the longest common prefix string amongst an array of strings.

'''



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""

        min_length = min(map(len, strs))

        ans = []
        for i in range(min_length):
            if len(set([str[i] for str in strs])) == 1:
                ans.append(strs[0][i])
            else:
                break
        return "".join(ans)


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["abcd", "abc", "ab"]))
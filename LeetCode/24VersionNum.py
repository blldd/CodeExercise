# -*- coding:UTF-8 -*-

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''



class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1_list = list(map(int, version1.split(".")))
        v2_list = list(map(int, version2.split(".")))


        max_length = max(len(v1_list), len(v2_list))

        if len(v1_list) < max_length:
            v1_list = v1_list + [0] * (max_length - len(v1_list))
        else:
            v2_list = v2_list + [0] * (max_length - len(v2_list))

        for i in range(max_length):
            if v1_list[i] < v2_list[i]:
                return -1
            if v1_list[i] > v2_list[i]:
                return 1

        if len(v1_list) == len(v2_list):
            return 0
        else:
            if len(v1_list) > len(v2_list):
                return 1
            else:
                return -1


if __name__ == '__main__':
    print(Solution().compareVersion("1.0", "1"))

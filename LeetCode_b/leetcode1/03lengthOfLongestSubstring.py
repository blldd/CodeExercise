class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        :param s:
        :return:
        """
        length = len(s)
        if length < 1:
            return 0

        char_idx_dict = {}
        res = 0
        last = -1
        for idx, ch in enumerate(s):
            if ch in char_idx_dict:
                last = max(char_idx_dict[ch], last)
            res = max(res, idx - last)
            char_idx_dict[ch] = idx
        return res

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 1:
            return 0

        used = {}
        max_len = 0
        left = -1
        for ind, w in enumerate(s):
            if w in used and left <= used[w]:
                left = used[w]
            else:
                max_len = max(max_len, ind - left)
            used[w] = ind
        return max_len


if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring1(s))

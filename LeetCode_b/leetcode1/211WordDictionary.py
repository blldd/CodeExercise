# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/2 11:29 AM
@Author  : ddlee
@File    : 211WordDictionary.py
"""

"""
211. 添加与搜索单词 - 数据结构设计
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tmp = self.dict

        for idx, ch in enumerate(word):
            if ch not in tmp:
                tmp[ch] = {}
            tmp = tmp[ch]
        tmp['end'] = True

    def search(self, word: str):

        def dfs(td, s):  # 深搜，参数为：当前子字典，当前串
            tmp = td
            for i, c in enumerate(s):
                if c == '.':
                    for j in tmp:
                        if j != 'end' and dfs(tmp[j], s[i + 1:]):
                            return True
                    return False

                if c not in tmp:
                    return False
                tmp = tmp[c]

            return 'end' in tmp

        return dfs(self.dict, word)


if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    obj.addWord("cab")

    print(obj.search("pad"))
    print(obj.search("bad"))
    print(obj.search(".ad"))
    print(obj.search("b.."))

# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/30 10:27 PM
@Author  : ddlee
@File    : 208Trie.py
"""

"""
208. 实现 Trie (前缀树)

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true

说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.keys = set()
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # self.keys.add(word)

        tmp = self.dict
        for char in word:
            if char not in tmp:
                tmp[char] = {}
            tmp = tmp[char]
        tmp['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        # """
        # return word in self.keys
        tmp = self.dict
        for char in word:
            if char not in tmp:
                return False
            else:
                tmp = tmp[char]
        return 'end' in tmp and tmp['end'] == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.dict
        for char in prefix:
            if char not in tmp:
                return False
            else:
                tmp = tmp[char]
        return True



if __name__ == '__main__':
    trie = Trie1()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))

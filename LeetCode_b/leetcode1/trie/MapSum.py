# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-07

"""Example Google style docstrings.
677. 键值映射

实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。
如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:

输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
"""


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for ch in key:
            node = node.setdefault(ch, {})
        node['val'] = val

    def sum1(self, prefix: str) -> int:
        node = self.trie
        for ch in prefix:
            if ch in node:
                node = node[ch]
            else:
                return 0

        def dfs(trie, res):

            for k, v in trie.items():
                if k == 'val':
                    res += v
                else:
                    res = dfs(v, res)
            return res

        res = 0
        res = dfs(node, res)

        return res

    def sum(self, prefix: str) -> int:
        node = self.trie
        for ch in prefix:
            if ch in node:
                node = node[ch]
            else:
                return 0

        def dfs(trie):

            for k, v in trie.items():
                if k == 'val':
                    nonlocal res
                    res += v
                else:
                    dfs(v)

        res = 0
        dfs(node)

        return res


if __name__ == '__main__':
    obj = MapSum()
    obj.insert("aa", 3)
    print(obj.sum("a"))

    obj.insert("ab", 2)
    print(obj.sum("a"))

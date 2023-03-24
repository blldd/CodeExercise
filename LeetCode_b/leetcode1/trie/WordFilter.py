# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-07

"""Example Google style docstrings.
745. 前缀和后缀搜索

给定多个 words，words[i] 的权重为 i 。

设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。
这个函数将返回具有前缀 prefix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。

例子:
输入:
WordFilter(["apple"])
WordFilter.f("a", "e") // 返回 0
WordFilter.f("b", "") // 返回 -1

注意:
words的长度在[1, 15000]之间。
对于每个测试用例，最多会有words.length次对WordFilter.f的调用。
words[i]的长度在[1, 10]之间。
prefix, suffix的长度在[0, 10]之前。
words[i]和prefix, suffix只包含小写字母。

"""


class WordFilter:

    def __init__(self, words):
        self.words = words
        self.map = {}
        self.indexmap = {}
        for i in range(len(words)):
            c = words[i][0]
            if c in self.map:
                self.map[c].append(words[i])
                self.indexmap[c].append(i)
            else:
                l1 = []
                l1.append(words[i])
                self.map[c] = l1
                l2 = []
                l2.append(i)
                self.indexmap[c] = l2

    def f(self, prefix: str, suffix: str) -> int:
        if prefix == None or prefix == "":  # 没有前缀条件，直接搜索后
            for i in range(len(self.words) - 1, -1, -1):
                if self.words[i].endswith(suffix):
                    return i

        else:  # 从相同首字母的单词中搜索
            c = prefix[0]
            if c not in self.map:
                return -1
            l1 = self.map[c]
            l2 = self.indexmap[c]
            for i in range(len(l1) - 1, -1, -1):
                if l1[i].startswith(prefix) and l1[i].endswith(suffix):
                    return l2[i]
        return -1


if __name__ == '__main__':
    words = ["apple"]
    obj = WordFilter(words)
    print(obj.f("a", "e"))
    print(obj.f("b", ""))

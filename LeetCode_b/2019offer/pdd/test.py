# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/27 9:47 PM
@Author  : ddlee
@File    : test.py
"""


def cut_words(text, tags):
    lxt = len(text)
    ltg = len(tags)
    if lxt < 1 or ltg < 1 or lxt != ltg or tags[0] != 'B':
        return []

    res = []
    tmp = ""
    for i, ch in enumerate(tags):
        if ch == 'B':
            if tmp != "":
                res.append(tmp)

            tmp = ""
            tmp += text[i]

        elif ch == 'I':
            tmp += text[i]

    if tmp:
        res.append(tmp)
    return res


text = "自然语言的研究员"
tags = "BIBIBBII"
print(cut_words(text, tags))

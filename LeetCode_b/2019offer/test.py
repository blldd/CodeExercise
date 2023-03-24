# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/13 7:24 PM
@Author  : ddlee
@File    : test.py
"""

pairs = [(1, 'one'), (2, 'two'), (2, 'three'), (4, 'four')]

pairs = sorted(pairs, key=lambda x: (-x[0], x[1]))
print(pairs)



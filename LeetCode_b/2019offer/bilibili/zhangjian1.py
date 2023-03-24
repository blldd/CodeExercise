# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(line):
    nums = "1234567890"
    # nums = list(map(str, list(range(10))))
    # print(nums)
    tags = ["+", "-"]

    max_length = 0
    max_str = ""

    tmp_str = ""

    flag = True
    dot_tag = False
    for idx, char in enumerate(line):
        if flag:
            if char in nums:
                tmp_str += char
            elif char in tags:
                if tmp_str != "":
                    max_str = tmp_str if len(tmp_str) >= len(max_str) else max_str
                    tmp_str = ""
                    flag = True
                else:
                    tmp_str += char
            elif char == "." and idx < len(line) and line[idx+1] in nums:
                if not dot_tag:
                    if tmp_str != "":
                        tmp_str += char
                        dot_tag = True
                    else:
                        tmp_str = ""
                        flag = True
                else:
                    max_str = tmp_str if len(tmp_str) >= len(max_str) else max_str
                    tmp_str = ""
                    dot_tag = False

            else:
                max_str = tmp_str if len(tmp_str) >= len(max_str) else max_str
                tmp_str = ""
        else:
            max_str = tmp_str if len(tmp_str) >= len(max_str) else max_str
            tmp_str = ""
            flag = True

    return max_str


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    # line1 = "1234567890abcd9.+12345.678.9ed"
    ans = process(line1)

    print(ans)


"""
1234567890abcd9.+12345.678.9ed

"""

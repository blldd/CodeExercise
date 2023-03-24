# -*- coding:UTF-8 -*-
"""
这样划分，我们只要求 a^b/2的值就可以的通过一次乘法运算求出a^b，依次求出，这就是快速幂，这样的操作的时间复杂度仅为O(logb)

代码如下，需要注意a和b可能为负数的问题。
"""


def quick_pow(a, b):
    tmpb = b
    if b < 0:
        tmpb = -b
    s = 1
    while tmpb != 0:
        if tmpb % 2 == 1:
            s = s * a
        a = a * a
        tmpb //= 2
    return 1.0 / s if b < 0 else s


def quick_pow1(a, b):
    tmpb = b
    if b < 0:
        tmpb = -b
    if b == 0:
        return 1
    if b == 1:
        return a
    s = 1

    if tmpb % 2 == 1:
        s = s * a
    tmp = quick_pow1(a, tmpb // 2)
    s *= (tmp * tmp)
    return 1.0 / s if b < 0 else s


if __name__ == '__main__':
    a = 2
    b = -5

    print(quick_pow1(a, b))

# -*- coding:UTF-8 -*-
import sklearn


def sqrt(x):
    if x < 2:
        return x
    left = 0
    right = x
    product = 1
    while abs(product - x) > 0.0001:
        mid = left + (right - left) / 2
        product = mid * mid
        if product < x:
            left = mid
        else:
            right = mid
    return int(mid)

def sqrt2(x):
    if x < 2:
        return x
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid < x:
            # left=mid
            left = mid + 1
            lstmid = mid  # 关键步骤啊，对于5这种情况啊
        elif mid * mid > x:
            # right=x
            right = mid - 1
        else:
            return mid
    return lstmid


if __name__ == '__main__':
    x = 10
    res = sqrt2(x)
    print(res)


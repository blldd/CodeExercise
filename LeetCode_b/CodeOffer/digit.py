import sys


def gen(num):
    b, q, r = 1, num, 0
    first, column, rest = 0, 1, 1
    lst = [0] * 9
    while q > 0:
        if r < q:
            q, r = divmod(num, b)
            skip = 1
        else:
            skip, r = divmod(r, q)
        b += skip
        if skip > rest:
            while skip > rest:
                lst[first] += q * rest
                skip -= rest
                first += 1
                if first >= 9:
                    first = 0
                    column *= 10
                rest = column
        lst[first] += q * skip
        rest -= skip
    return lst


l, r = [int(s) for s in input().split(' ')]
ans1 = gen(l - 1)
ans2 = gen(r)
for i in range(9):
    print(ans2[i] - ans1[i])

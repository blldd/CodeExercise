# -*- coding:UTF-8 -*-

import time, functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t1 = time.time()
        func(*args, **kw)
        print('%s excute in %s ms' % (func.__name__, 1000 * (time.time() - t1)))

    return wrapper


@log
def slow(x, y, z):
    time.sleep(5)


@log
def fast(x, y):
    time.sleep(2)


slow(4, 5, 6)
fast(3, 5)

print(slow.__name__)

# -*- coding:UTF-8 -*-
import collections




def containsNearbyAlmostDuplicate(nums, k, t):
    if k < 0 or t < 0:
        return False
    window = collections.OrderedDict()
    for n in nums:
        # Make sure window size
        if len(window) > k:
            window.popitem(False)

        print
        window

        bucket = n if not t else n // t

        print
        bucket

        # At most 2t items.
        for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
            if m is not None and abs(n - m) <= t:
                return True
        window[bucket] = n
    return False


if __name__ == '__main__':
    nums = [0, 9, 4, 2, 8, 3]
    k = 2
    t = 2
    print(containsNearbyAlmostDuplicate(nums, k, t))
# -*- coding:UTF-8 -*-

def median_of_two_sorted_arr(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0

def get_up_median(shorts, s1, e1, longs, s2, e2):
    while s1 < e1:
        mid1 = (s1 + e1) // 2
        mid2 = (s2 + e2) // 2
        offset = ((e1 - s1 + 1) & 1) ^ 1
        if shorts[mid1] > longs[mid2]:
            e1 = mid1
            s2 = mid2 + offset
        elif shorts[mid1] < longs[mid2]:
            s1 = mid1 + offset
            e2 = mid2
        else:
            return shorts[mid1]

    return min(shorts[s1], longs[s2])


def find_kth_num(arr1, arr2, kth):
    """
    给定两个一维int数组A和B. 其中:
    A是长度为m、元素从小到大排好序的有序数组。
    B是长度为n、元素从小到大排好序的有序数组。
    希望从A和B数组中，找出最大的k个数字，
    要求:使用尽量少的比较次数。
    """
    if len(arr1) < 0 or len(arr2) < 0:
        return None
    if kth < 1 or kth > len(arr1) + len(arr2):
        return None
    longs = arr1 if len(arr1) >= len(arr2) else arr2
    shorts = arr1 if len(arr1) < len(arr2) else arr2
    l = len(longs)
    s = len(shorts)
    if kth <= s:
        return get_up_median(shorts, 0, kth - 1, longs, 0, kth - 1)
    if kth > l:
        if shorts[kth - l - 1] >= longs[l - 1]:
            return shorts[kth - l - 1]
        if longs[kth - s - 1] >= shorts[s - 1]:
            return longs[kth - s - 1]
        return get_up_median(shorts, kth - l, s - l, longs, kth - s, l - 1)
    if longs[kth - s - 1] >= shorts[s - 1]:
        return longs[kth - s - 1]
    return get_up_median(shorts, 0, s - 1, longs, kth - s, kth - 1)



if __name__ == '__main__':
    nums1 = [1, 2, 2, 4]
    nums2 = [1, 3, 3, 4, 5]
    print(median_of_two_sorted_arr(nums1, nums2))

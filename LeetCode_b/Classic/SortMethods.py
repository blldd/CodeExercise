# -*- coding:UTF-8 -*-
# import pysnooper

from util_tools import *

quick_sort_lam = lambda array: array if len(array) <= 1 else \
    quick_sort_lam([item for item in array[1:] if item <= array[0]]) \
    + [array[0]] + \
    quick_sort_lam([item for item in array[1:] if item > array[0]])


# @excute_time_log
# @pysnooper.snoop()
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] >= key:
            right -= 1
        array[left], array[right] = array[right], array[left]
        while left < right and array[left] <= key:
            left += 1
        array[right], array[left] = array[left], array[right]
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


def quick_sort_recur(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort_recur(array, l, q - 1)
        quick_sort_recur(array, q + 1, r)


def partition(nums, left, right):
    key = nums[left]
    while left < right:
        # right下标位置开始，向左边遍历，查找不大于基准数的元素
        while left < right and nums[right] >= key:
            right -= 1
        if left < right:  # 找到小于准基数key的元素,然后交换nums[left],nums[right]
            nums[left], nums[right] = nums[right], nums[left]
        else:  # left〉=right 跳出循环
            break
        # left下标位置开始，向右边遍历，查找不小于基准数的元素
        while left < right and nums[left] < key:
            left += 1
        if left < right:  # 找到比基准数大的元素，然后交换nums[left],nums[right]
            nums[right], nums[left] = nums[left], nums[right]
        else:  # left〉=right 跳出循环
            break
    return left  # 此时 left==right 所以返回right也是可以的


def partition1(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort_stack(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


def bubble_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    for i in range(length):
        for j in range(i, length):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def countingSort(arr):  # the elements in the array are all integers
    maximum, minimum = max(arr), min(arr)
    countArr = [0] * (maximum - minimum + 1)
    for i in arr:  # record the number of times of every element in the array
        countArr[i - minimum] += 1
    # print(countArr)

    for i in range(1, len(countArr)):  # calculate the position of every element
        countArr[i] += countArr[i - 1]
    # print(countArr)

    targetArr = [None] * len(arr)
    for i in range(len(arr) - 1, -1, -1):  # reverse-order traversal is for the stability
        countIndex = arr[i] - minimum
        targetArr[countArr[countIndex] - 1] = arr[i]
        countArr[countIndex] -= 1
    return targetArr


if __name__ == '__main__':
    input = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
    input = [3, 5, 7, 8, 6, 4, 1, 2, 3]

    print(countingSort(input))

    quick_sort(input, 0, 8)
    print(input)
    # input.sort()
    # res = quick_sort_lam(input)
    # print(res)
    # quick_sort_recur(input, 0, 13)
    # print(input)
    # quick_sort_stack(input, 0, 13)
    # print(input)
    input = [4, 4, 3, 1, 8]
    print(bubble_sort(input))
    #
    # start = time.time()
    # rand = np.random.randint(1000, size=1000)
    # quick_sort(rand, 0, 999)
    # end = time.time()
    # print(end - start)
    #
    # start = time.time()
    # rand = np.random.randint(1000, size=1000)
    # bubble_sort(rand)
    # end = time.time()
    # print(end - start)
    #
    # start = time.time()
    # rand = list(range(100))
    # quick_sort(rand, 0, 99)
    # end = time.time()
    # print(end - start)
    #
    # start = time.time()
    # rand = list(range(100))
    # bubble_sort(rand)
    # end = time.time()
    # print(end - start)

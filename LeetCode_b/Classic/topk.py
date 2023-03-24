# -*- coding:UTF-8 -*-

def down_adjust_min(array, parentIndex, length):
    temp = array[parentIndex]
    childIndex = 2 * parentIndex + 1
    while (childIndex < length):
        if childIndex + 1 < length and array[childIndex + 1] < array[childIndex]:
            childIndex += 1
        if temp <= array[childIndex]:
            break
        array[parentIndex] = array[childIndex]
        parentIndex = childIndex
        childIndex = 2 * childIndex + 1
    array[parentIndex] = temp


def heap_sort(array):
    """
    堆排序算法的步骤：
    1. 把无序数组构建成二叉堆。
    2. 循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶。
    :param array:
    :return:
    """
    # 1.构建二叉堆
    for i in range(int(len(array) / 2))[::-1]:
        down_adjust_min(array, i, len(array))
    print(array)

    # 2.循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶
    for i in range(len(array))[::-1]:
        array[i], array[0] = array[0], array[i]
        down_adjust_min(array, 0, i)
    print(array)


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


if __name__ == '__main__':
    bigdata = [6, 4, -9, 10, 3, 2, 14, 5, 6, 4, 3, 2, 6, 5, 444, 665, 4, 3]
    heap_sort(bigdata)

    quick_sort(bigdata, 0, 17)
    print(bigdata)

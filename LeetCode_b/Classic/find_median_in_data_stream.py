# -*- coding:UTF-8 -*-

class MedianFinder(object):
    def __init__(self):
        """
        想法：
            构建两个堆，大根堆，小根堆，保证大根堆的最大值 比 小根堆的最小值 小，保证两个堆相差不超过2
            这样中位数就可以通过计算堆顶元素获得，时间复杂度O（1）
            堆调整的复杂度O（logn）

        """
        self.arr = []
        self.max_heap = []
        self.min_heap = []
    #
    # def addNum(self, x):
    #     self.arr.append(x)
    #
    # def findMedian(self):
    #     length = len(self.arr)
    #     if length < 1:
    #         return None
    #
    #     if length == 1:
    #         return self.arr[0]
    #     self.quick_sort(self.arr)
    #
    #     mid = length // 2
    #     if length % 2 == 0:
    #         return self.arr[mid]
    #     else:
    #         return (self.arr[mid - 1] + self.arr[mid]) / 2
    #
    # def quick_sort(self, arr, left, right):
    #     length = len(arr)
    #     if length < 2:
    #         return arr
    #
    #     low = left
    #     high = right
    #     pivot = arr[0]
    #
    #     while left < right:
    #         while left < right and arr[right] >= pivot:
    #             right -= 1
    #     arr[left], arr[right] = arr[right], arr[left]
    #     while left < right and arr[left] <= pivot:
    #         left += 1
    #     arr[right], arr[left] = arr[left], arr[right]
    #
    #     self.quick_sort(arr, low, left - 1)
    #     self.quick_sort(arr, left + 1, high)

    def add_num(self, num):
        self.max_heap.append(num)
        self.down_ajust_max(self.max_heap)

        self.min_heap.append(self.max_heap.pop(0))
        self.down_ajust_min(self.min_heap)

        if len(self.max_heap) < len(self.min_heap):
            self.max_heap.append(self.min_heap.pop(0))
            # self.down_ajust_min(self.min_heap)
            self.down_ajust_max(self.max_heap)

    def down_ajust_max(self, arr):
        length = len(arr)
        if length < 2:
            return arr

        parent_idx = 0
        tmp = arr[parent_idx]
        child_idx = 2 * parent_idx + 1
        while child_idx < length:
            if child_idx + 1 < length and arr[child_idx + 1] > arr[child_idx]:
                child_idx += 1
            if tmp > arr[child_idx]:
                break
            arr[parent_idx] = arr[child_idx]
            parent_idx = child_idx
            child_idx = 2 * child_idx + 1
        arr[parent_idx] = tmp

    def down_ajust_min(self, arr):
        length = len(arr)
        if length < 2:
            return arr

        parent_idx = 0
        tmp = arr[parent_idx]
        child_idx = 2 * parent_idx + 1
        while child_idx < length:
            if child_idx + 1 < length and arr[child_idx + 1] < arr[child_idx]:
                child_idx += 1
            if tmp < arr[child_idx]:
                break
            arr[parent_idx] = arr[child_idx]
            parent_idx = child_idx
            child_idx = 2 * child_idx + 1
        arr[parent_idx] = tmp

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.max_heap[0]


if __name__ == '__main__':
    mf = MedianFinder()
    mf.add_num(5)
    mf.add_num(4)
    mf.add_num(9)
    mf.add_num(7)
    mf.add_num(3)
    print(mf.min_heap)
    print(mf.max_heap)
    print(mf.find_median())

    # import heapq
    #
    # # 向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
    # heapq.heappush()
    # # heapq把列表x转换成堆
    # heapq.heapify()
    # # 从可迭代的迭代器中返回最大的n个数，可以指定比较的key
    # heapq.nlargest()
    # # 从可迭代的迭代器中返回最小的n个数，可以指定比较的key
    # heapq.nsmallest()
    # # 从堆中删除元素，返回值是堆中最小或者最大的元素
    # heapq.heappop()


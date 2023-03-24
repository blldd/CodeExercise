


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


def sortArray(nums):
    l = len(nums)
    if l < 2:
        return nums
    quick_sort(nums, 0, l-1)
    return nums
        

quick_sort_lam = lambda array: array if len(array) <= 1 else \
    quick_sort_lam([item for item in array[1:] if item <= array[0]]) \
    + [array[0]] + \
    quick_sort_lam([item for item in array[1:] if item > array[0]])

if __name__ == '__main__':
    nums = [5,2,3,1]
    nums = [2,8,4,1,3,5,6,7]
    nums = sortArray(nums)    
    # nums = quick_sort_lam(nums)
    print(nums)





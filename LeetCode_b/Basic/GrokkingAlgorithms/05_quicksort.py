
def quicksort(array):
    if len(array) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # recursive case
        pivot = array[0]  #
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]   # O(n)
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot] # O(n)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))

# O(nlogn)

# arr = [1, 2]
# arr2 = [3, 4]
# print((arr + arr2))

# 2 ** x = n
# x = logn
# O(logn)
# n
#        1
#       / \
#       2  3
#     /\   /\
#     4 5 6 7
#    /\/\ /\/\
#   8 9 10 ...

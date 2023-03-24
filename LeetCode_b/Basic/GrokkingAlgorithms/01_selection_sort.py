# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest_idx = findSmallest(arr)
      newArr.append(arr.pop(smallest_idx))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))
# O(n2)

arr = [5, 3, 6, 2, 10]
a = arr.pop()
print(a)
print(arr)

b = arr.pop(3)
print(b)
print(arr)
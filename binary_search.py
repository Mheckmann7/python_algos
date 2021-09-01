def binary_search(arr, low, high, num): 
    # high starts at end of arr low starts at first element 
    if high >= low: # 
        mid = (high + low) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:  # if the element is smaller than the mid then it must be in the left sub array
            binary_search(arr, low, mid - 1, num) #search again with the low and one element before the mid
        elif arr[mid] < num: # if the element is higher than the mid then it must be in the right
            binary_search(arr, mid + 1, high, num) #search again with the hight and one element after the mid 
    else: 
        return -1 # element is not in the array 


arr = [2,3,4,10,40]
# print(binary_search(arr, 0, len(arr) - 1, 10))


def search(arr, num):
    left = 0
    right = arr.length - 1
    while left <= right:
        mid = (left + right) / 2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1 
    return -1 
#Given a sorted array of integers, return the low and high index of the given key. 
# You must return -1 if the indexes are not found.
def find_low_index(arr, key):
  
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:

    mid_elem = arr[mid]

    if mid_elem < key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2)

  if low < len(arr) and arr[low] == key:
    return low

  return -1

def find_high_index(arr, key):
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:
    mid_elem = arr[mid]

    if mid_elem <= key:
      low = mid + 1
    else:
      high = mid - 1

    mid = low + int((high - low) / 2);
  
  if high == -1:
    return high

  if high < len(arr) and arr[high] == key:
    return high

  return -1


array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))
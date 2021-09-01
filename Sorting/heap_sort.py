def heapify(arr, n, i):
    largest = i # initialize largest as the root
    left = 2 * i + 1 
    right = 2 * i + 1

    if left < n and arr[largest] < arr[left]: 
        # see if left child of root exists and is greater than the root 
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
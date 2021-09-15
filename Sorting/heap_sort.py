def heapify(arr, n, i):
    largest = i # initialize largest as the root
    left = 2 * i + 1 
    right = 2 * i + 1

    if left < n and arr[largest] < arr[left]: 
        # see if left child of root exists and is greater than the root 
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i: # if largest is not the root object swap it 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

    
def heapSort(arr):
    n = len(arr)
    # build max heap 
    for i in range(n // 2 - 1, -1, -1): #start at the middle and go back to 0, find root nodes
        heapify(arr, n ,i)
    # extract elements from the root one by one 
    for i in range(n -1, 0 , -1): # start at the end and go back to 1 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)

# in place algorithm 
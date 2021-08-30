#Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array

def move_zeros(arr):
    if len(arr) < 1: 
        return
    
    write = len(arr) - 1
    read = len(arr) - 1

    while(read >= 0):
        if arr[read] != 0: # if arr element does not equal 0 
            print('before', arr[write])
            arr[write] = arr[read] # place the read element into the 
            print('after', arr[write])
            write -= 1
        read -= 1 
        print('read', read, 'write', write)
    while(write >= 0):
        arr[write] = 0
        write -= 1 

print(move_zeros([2,3,5,0,4,0,2]))
# Tries to find the min value in the list, 
# once the min value is found it is moved to the begining of the list
def selection_sort(lst): 
    indexing_length = range(0, len(lst) - 1) 
    #once we have the last item in the list we don't need to compare it we can assume that is the highest value in the list

    for i in indexing_length: 
        #for every element in the indexing length, set the min value = i
        # for every iteration we want the first element in the unsorted list to be the default min
        min_value = i 
        # min = 0
        for j in range(i + 1, len(lst)): # all elements to the right of current index 
            if lst[j] < lst[min_value]: # go through ALL elements to the right of the current index
                # if we find something smaller make the swap
                #[7, 8, 4, 6, 8, 20, 3, 11, 23] j = 6
                min_value = j # we don't need to make a swap everytime we reach a min value 
                # do the swap with the min values position at the very end 
        if min_value != i: 
            # if we find an item that has a lower value than our default we need to switch those items
            lst[min_value], lst[i] = lst[i], lst[min_value] #[3, 8, 4, 6, 8, 20, 7, 11, 23]
    return lst

print(selection_sort([7,8,4,6,8,20,3,11,23]))
# cuts down the number of item switches that we need to do
# we also only have to go through through the unsorted portion of the list 
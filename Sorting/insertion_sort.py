# Insert the item in the correct position 

def insertion_sort(lst): 
    indexing_length = range(1, len(lst)) 
    # first item is already in our sorted list since it is all the way to the left

    for i in indexing_length:
        value_to_sort = lst[i] # look at lst[1]
        print('value',value_to_sort)
        while lst[i - 1] > value_to_sort and i > 0: 
            # value to the left is higher than the value we are currently trying to sort 
            # while item to left is > value to right
            # i>0 prevents negative indexing
            lst[i], lst[i -1] = lst[i -1], lst[i]
            # continue to do swaps while left is > than right 
            i = i - 1
            # incrementally stepping down the list using i because you are always comparing to the number before
            print(i)
            print(lst)
         

    return lst


#[4,5,52,56]
# 0 1 2 3

# optimized version 
def insertion_sort_op(list_to_be_sorted):
    for i in range(1, len(list_to_be_sorted)):
        key = list_to_be_sorted[i]
        j = i - 1
        while j >= 0 and key < list_to_be_sorted[j]:
            list_to_be_sorted[j + 1] = list_to_be_sorted[j]
            j -= 1
        list_to_be_sorted[j + 1] = key
    return list_to_be_sorted

print(insertion_sort_op([4,52,5,56,7,82,3,52,1]))
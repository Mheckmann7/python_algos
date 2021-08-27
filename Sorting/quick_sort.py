# takes the last item and makes it the pivot, iterates through all the values 

def quick_sort(lst): 
    if len(lst) <= 1: 
        return lst 
    else: 
        pivot = lst.pop() # get the last item in the list
    items_greater = []
    items_lower = []

    for item in lst: # for every item left in the sequence 
        if item > pivot: 
            items_greater.append(item) # append the item to the greater than list
        else: 
            items_lower.append(item) # else append the item to the less than list 
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) 
    # concat the items to the pivot 
    # use recursion to call the algorithm on each of the sublists 

print(quick_sort([23,34,56,76,45,23,24,20])) 
# often out performs with n log n complexity 
# Find the minimum value and place it in the last iteration of the sorted list

def selection_sort(lst): 
    indexing_length = range(0, len(lst) - 1)

    for i in indexing_length:
        min_value = i 

        for j in range(i + 1, len(lst)): 
            if lst[j] < lst[min_value]:
                min_value = j

        if min_value != i: 
            lst[min_value], lst[i] = lst[i], lst[min_value]
    return lst

print(selection_sort([7,8,4,6,8,20,3,11,23]))
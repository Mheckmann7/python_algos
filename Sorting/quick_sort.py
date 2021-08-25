def quick_sort(lst): 
    if len(lst) <= 1: 
        return lst
    else: 
        pivot = lst.pop()
    items_greater = []
    items_lower = []

    for item in lst: 
        if item > pivot:
            items_greater.append(item)
        else: 
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([23,34,56,76,45,23,24,20]))
#divides the input array into two halves, calls itself for the two halves and then merges the two halves

def merge_sort(list):
    if len(list) > 1: 
        left_list = list[:len(list)//2] #starts at 0 and goes to the len of the list / 2
        right_list = list[len(list)//2:] #starts at length of list / 2 and goes to the end

         #recursion 
        merge_sort(left_list)
        merge_sort(right_list)
        print(left_list, right_list)
         #merge
        i = 0 # left most element in left list
        j = 0 # left most element in right list
        k = 0 # merged list index
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]: # left list is smaller than right list
                list[i] = left_list[i] #save the value of the left list inside the merged list
                i += 1 # increase i
            else: # right list is smaller than the left list at the current index or they are equal
                list[k] = right_list[j]
                j += 1
            k += 1 #increase k in every while loop 
        # check if any elements were left over 
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1 

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
    return list

print(merge_sort([6,4,6,7,11,9,2,10]))
# very efficient for large data sets
# log n merge steps because merge sort doubles the list size
# n work for each merge step because if must look at every item
# so O(n log n)



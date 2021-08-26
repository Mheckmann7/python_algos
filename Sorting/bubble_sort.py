# Swaps adjacent elements if they are in the incorrect order. 
# Iterates over the list until all elements have been sorted

def bubble_sort(lst):
	indexing_length = len(lst) - 1 
    # can’t perform a comparison on last # of list because there is nothing after it to compare to
	sorted = False
    # breaks the loop whenever the list is sorted
	while not sorted: 
		sorted = True
		for i in range(0, indexing_length):
			if lst[i] > lst[i + 1]: 
                # if the value to the left is greater than the value to the right
				sorted = False
                # set sorted to false
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # swap the adjacent elements 
        # When all of the elements have been sorted the if statement wont be called
        # So sorted = True and the loop will be broken
	return lst

print(bubble_sort([4,3,5,3,6,7,8,9,2]))
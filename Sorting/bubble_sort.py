def bubble_sort(lst):
	indexing_length = len(lst) - 1 # can’t perform a comparison on last # of list
	sorted = False

	while not sorted: 
		sorted = True
		for i in range(0, indexing_length):
			if lst[i] > lst[i + 1]:
				sorted = False
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
	return lst

print(bubble_sort([4,3,5,3,6,7,8,9,2]))
#Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 

def sum_two_values(arr, value):
    found_values = set()
    for i in arr: 
        if value - i in found_values:
            return True
        found_values.add(i)
    return False
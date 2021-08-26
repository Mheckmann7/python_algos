from math import sqrt
def is_prime(num):
    flag = 0
    if num <= 1: 
        return False
    for i in range(2, int(sqrt(num))+1): 
        if(num % i ==0):
            flag= 1
            return False
    if flag == 0: 
        return True
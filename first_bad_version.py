# out of n versions find which version is the first bad one 

def firstBadVersion(n):
    left = 0 
    right = n #5 
        
    while left < right: # 0 5  
        mid = (left + right) // 2  #2
        if isBadVersion(mid): #
            right = mid #
        else:
            left = mid + 1 # 
    return right 
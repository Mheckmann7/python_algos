class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def merge_intervals(arr):
    if len(arr) == 0:
        return
    result = []
    result.append(Pair(arr[0].first, arr[0].second)) #append the first pair 
    print('result', result)
    for i in range(1, len(arr)):
        x1 = arr[i].first #first of index 1
        y1 = arr[i].second #second of index 1 
        x2 = result[len(result) - 1].first # the end of the results arr
        y2 = result[len(result) - 1].second # the results arr 
        if y2 >= x1:
            result[len(result) -1].second = max(y1,y2)
            # set the larger second # of the two to  
        else: result.append(Pair(x1,y1))
        print(x1,y1,x2,y2, result[i] - 1)
    return result 


arr = [Pair(1, 5), Pair(3, 7), Pair(4, 6), 
     Pair(6, 8), Pair(10, 12), Pair(11, 15)]

print(merge_intervals(arr))
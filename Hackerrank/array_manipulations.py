# Array Manipulation

# SOLUTIONS 1
from collections import Counter
def arrayManipulation(n, queries):
    dict_arr = Counter()
    max_num = 0
    arr_num = 0
    for a, b, k in queries:
        dict_arr[a] += k
        dict_arr[b+1] -= k
    for i in sorted(dict_arr):
        arr_num += dict_arr[i]
        max_num = max(max_num, arr_num)
    return max_num
    
    

# SOLUTIONS 2
from collections import Counter
def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum
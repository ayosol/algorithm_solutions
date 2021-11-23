def simpleSort(arr):
    
    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j += 1
    return arr


# Write a function that, given an array of integers arr, sorts its elements in ascending order.
def selection_sort(arr):
    for i in range(0,len(arr)):
        min = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < min:
                min = arr[j]
                x = j
        arr[i], arr[x] = arr[x], arr[i]

    return arr

arr = [1,5,6,8,3,4,0,2,7]
print selection_sort(arr)

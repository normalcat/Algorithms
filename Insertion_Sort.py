def insertion_sort(arr):
    arr_new = []
    for i in range(0,len(arr)):
        x = False
        for j in range(0,i):
            if arr[i] < arr_new[j]:
                arr_new.insert(j,arr[i])
                x = True
                break
        if not x:
            arr_new.append(arr[i])
    return arr_new

arr = [2,5,8,1,7,3,4,6]
print insertion_sort(arr)

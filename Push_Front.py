def push_front(arr, val):
    arr.append(val)
    for i in range(0,len(arr)-1):
        arr[len(arr)-1-i], arr[len(arr)-2-i] = arr[len(arr)-2-i], arr[len(arr)-1-i]
    return arr

arr = [1,6,9,10]
print push_front(arr,11)

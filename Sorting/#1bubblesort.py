def bubble(arr):
    swap = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap = True
        if (not swap):
            break
 
arr = [2,34,1,3,4,5,2]
bubble(arr)
print(arr)
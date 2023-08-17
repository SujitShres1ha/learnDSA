def InsertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, 0, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            else:
                break

    return arr

print(InsertionSort([5, 4, 3, 2, 1]))

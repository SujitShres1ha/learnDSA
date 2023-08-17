def CycleSort(arr):
    i = 0
    while (i < len(arr)):
        correct = arr[i] - 1
        if (arr[i] == arr[correct]):
            i += 1
        else:
            swap(arr,i,correct)
    return arr

def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

print (CycleSort([5,4,3,2,1]))
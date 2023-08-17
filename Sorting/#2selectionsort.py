def SelectionSort(arr):
    for i in range(len(arr)):
        max = findMax(arr,0,len(arr)-i)
        swap(arr,max,len(arr)-i-1)
    return arr


def findMax(arr,start,end):
    max = start
    for i in range(start,end):
        if arr[max]<arr[i]:
            max = i
    return max

def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

print (SelectionSort([5,4,3,2,1]))
def find_ceiling(arr,target):
    start = 0
    end = len(arr) - 1
    while (start<=end):
        mid = (start+end) // 2
        if (target>arr[mid]):
            start = mid + 1
        else :
            end = mid - 1
        if (target == arr[mid]):
            return mid
    return start

print(find_ceiling([2,3,4,9,16,18],10))
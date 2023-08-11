def find_pivot(arr):
        start = 0
        end = len(arr) - 1 
        while (start <= end):
            mid = (start + end) // 2
            if mid < end and arr[mid] > arr[mid + 1]:
                return mid
            if mid > start and arr[mid - 1] > arr[mid]:
                return mid - 1
            if arr[start] == arr[mid] == arr[end]:
                # Handle case when arr[start] == arr[mid] == arr[end]
                if start<end and arr[start] > arr[start + 1]:
                    return start
                if arr[end-1] > arr[end]:
                    return end-1
                start = start + 1
                end = end - 1
            elif arr[start] <= arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1
count = find_pivot([8,8,9,6,7,8])
print(count+1)
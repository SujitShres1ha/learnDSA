class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        peak = self.peakIndexInMountainArray(mountain_arr)
        find = self.search(target, mountain_arr, 0, peak)
        if find != -1:
            return find
        else:
            find = self.search(target, mountain_arr, peak, len(mountain_arr) - 1)
            return find

    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid + 1] < arr[mid]:
                end = mid
            else:
                start = mid + 1
        return start

    def search(self, target, arr, start, end):
        asc = arr[start] < arr[end]
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            if asc:
                if target > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target < arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1



sol = Solution()
print(sol.findInMountainArray(2,[0,2,4,2,1]))

   
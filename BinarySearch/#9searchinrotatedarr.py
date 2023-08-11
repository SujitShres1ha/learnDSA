class Solution:
    def search(self, nums, target) :
        pivot = self.find_pivot(nums)
        search1 = self.searchRange(target,nums,0,pivot)
        search2 = self.searchRange(target, nums, pivot + 1, len(nums) - 1)
        if (nums[search1]==target or nums[search2]==target):
            return True
        else:
            return False
    def find_pivot(self,arr):
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
    def searchRange(self,target, arr, start, end):
        while (start<=end):
            mid = (start+end)//2
            if target > arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                return mid
            
        return -1


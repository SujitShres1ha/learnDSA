class Solution:
    def search(self, nums, target) :
        pivot = self.find_pivot(nums)
        search1 = self.searchRange(target,nums,0,pivot)
        if (search1==-1):
            return self.searchRange(target,nums,pivot+1,len(nums)-1)
        else:
            return search1


    def find_pivot(self,arr):
        start = 0
        end = len(arr) - 1
        while (start<=end):
            mid = (start+end)//2
            if (mid < end and arr[mid]>arr[mid+1]):
                return mid
            if (mid > start and arr[mid-1]>arr[mid]):
                return mid-1
            if (arr[start] < arr[mid]):
                start = mid + 1
            else:
                end = mid - 1
        return -1
    def searchRange(self,target, arr, start, end):
        while (start<=end):
            mid = (start+end)//2
            if (target>arr[mid]):
                start = mid + 1
            elif (target<arr[mid]):
                end = mid - 1
            else:
                return mid
            
        return -1

sol = Solution()
print(sol.search([6,7,1,2,3,4,5],6))
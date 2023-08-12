class Solution():
    def search(self,nums,target):
        peak = self.findPeak(nums)
        target_index = self.searchTarget(nums,target,peak+1,len(nums)-1)
        if (target_index==True):
            return target_index
        else:
            return self.searchTarget(nums,target,0,peak)



    def findPeak(self,nums):
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if (mid > start and nums[mid-1]>nums[mid]):
                return mid - 1
            if (mid<end and nums[mid]>nums[mid+1]):
                return mid
            if (nums[start]==nums[mid]==nums[end]):
                if start<end and nums[start]>nums[start+1]:
                    return start
                if start<end and nums[end-1]>nums[end]:
                    return end-1
                start += 1
                end -= 1
            elif (nums[start]<=nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
            
            
        return mid

    def searchTarget(self,nums,target,start,end):
        while(start<=end):
            mid = (start+end)//2
            if (target>nums[mid]):
                start = mid+1
            elif (target<nums[mid]):
                end = mid - 1
            else:
                return True
        return False

sol = Solution()
print(sol.search([3,0,0,1,2,2],3))
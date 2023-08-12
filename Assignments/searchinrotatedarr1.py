class Solution():
    def search(self,nums,target):
        peak = self.findPeak(nums)
        target_index = self.searchTarget(nums,target,peak+1,len(nums)-1)
        if (target_index!=-1):
            return target_index
        else:
            return self.searchTarget(nums,target,0,peak)



    def findPeak(self,nums):
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if (start<end and nums[start]>nums[start+1]):
                return start
            elif (mid<end and nums[mid]>nums[mid+1]):
                end = mid
            else:
                start += 1
        print(mid)
        return mid

    def searchTarget(self,nums,target,start,end):
        while(start<=end):
            mid = (start+end)//2
            if (target>nums[mid]):
                start = mid+1
            elif (target<nums[mid]):
                end = mid - 1
            else:
                return mid
        return -1

sol = Solution()
print(sol.search([5,1,3],5))
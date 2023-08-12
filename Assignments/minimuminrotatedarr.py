class Solution:
    def findMin(self, nums):
        peak = self.findPeak(nums)
        print(nums[peak])
        if (nums[len(nums)-1] == nums[peak]):
            return nums[0]
        else:
            return nums[peak+1]




    def findPeak(self,nums):
        start = 0
        end = len(nums) - 1
        
        while (start<=end):
            mid = (start+end)//2
            if (mid < end and nums[mid]>nums[mid+1]):
                return mid
            if (mid > start and nums[mid-1]>nums[mid]):
                return mid-1
            if (nums[start] < nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        return -1
        

sol = Solution()
print(sol.findMin([2,1]))
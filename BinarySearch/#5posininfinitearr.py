class Solution(object):
    def searchRange(self, nums,target):
        start = 0
        end = 1
        while (target>nums[end]):
            temp = end
            end = end + (end-start+1)*2
            start = temp + 1
        print(self.search(nums,start,end,target))
        
    def search(self,nums,start,end,target):
        while (start<=end):
            mid = (start+end)//2
            if (target > nums[mid]):
                start = mid + 1
            elif (target < nums[mid]):
                end = mid - 1
            else:
                return mid
        return -1
sol = Solution()
sol.searchRange([2,3,4,5,6,7,8],6)
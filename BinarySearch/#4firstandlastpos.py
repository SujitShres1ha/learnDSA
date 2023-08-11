class Solution(object):
    def searchRange(self, nums,target):
        lst = [-1,-1]
        lst[0] = self.find_pos(nums,target,True)
        if (lst[0]!=-1):
            lst[1] = self.find_pos(nums,target,False)
        return lst

    def find_pos(self,nums,target,firstpos):
        start = 0
        end = len(nums) - 1
        ans = -1
        while (start<=end):
            mid = (start+end)//2
            if (target > nums[mid]):
                start = mid + 1
            elif (target < nums[mid]):
                end = mid - 1
            else:
                ans = mid
                if (firstpos):
                    end = mid - 1
                else:
                    start = mid + 1
        return ans
sol = Solution()
print(sol.searchRange([1,2,2,3,4,],0))
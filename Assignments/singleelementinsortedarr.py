class Solution():
    def singleNonDuplicate(self,nums):
        start = 0
        end = len(nums) - 1
        while (start<=end):
            if (start<end):
                if (nums[start]!=nums[start+1]):
                    return nums[start]
                else:
                    start+=2
                if (nums[end]!=nums[end-1]):
                    return nums[end]
                else:
                    end-=2
            else:
                return nums[start]
        
sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
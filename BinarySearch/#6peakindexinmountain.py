class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr)-1
        while(start<end):
            mid = (start+end)//2
            if (arr[mid+1]<arr[mid]):
                end = mid
            else: 
                start = mid+1
        return start

sol = Solution()
print (sol.peakIndexInMountainArray([0,1,0]))
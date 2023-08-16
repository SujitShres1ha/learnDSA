class Solution:
    def maxValue(self,n,index, maxSum):
        start = 1
        end = maxSum
        l = index
        r = n - index - 1
        while start<=end:
            mid = (start+end)//2
            m = mid - 1
            if (l<=m):
                ls = m*(m+1)//2 - (m-l)*(m-l+1)//2
            else:
                ls = m*(m+1)//2 + (l-m)
            if (r<=m):
                rs = m*(m+1)//2 - (m-r)*(m-r+1)//2
            else:
                rs = m*(m+1)//2 + (r-m)
            if (mid + ls + rs)<=maxSum:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1     
        return ans      

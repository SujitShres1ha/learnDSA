class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start = 0
        end = len(letters) - 1
        
        while(start<=end):
            mid = (start+end)//2
            if (target<letters[mid]):
                end = mid - 1
            else:
                start = mid + 1
            if (start == len(letters)):
                return letters[0]
        return letters[start]


sol = Solution()    
print(sol.nextGreatestLetter(['c','f','g'],'c'))

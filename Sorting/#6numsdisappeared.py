class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        sorted_nums = self.CycleSort(nums)
        print(sorted_nums)
        lst = []
        for i in range(0,len(sorted_nums)):
            if sorted_nums[i] != i + 1:
                lst.append(i+1)
        return lst




    def CycleSort(self,arr):
        i = 0
        while (i < len(arr)):
            correct = arr[i] - 1
            if (arr[i] == arr[correct]):
                i += 1
            else:
                self.swap(arr,i,correct)
        return arr

    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp

sol = Solution()
print(sol.findDisappearedNumbers([1,1]))
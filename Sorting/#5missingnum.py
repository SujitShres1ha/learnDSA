class Solution:
    def missingNumber(self, arr: list[int]) -> int:
        sorted_arr = self.CycleSort(arr)
        for i in range(0,len(arr)):
            if (sorted_arr[i] != i):
                return i
        return len(arr)

    def CycleSort(self,arr):
        i = 0
        while (i < len(arr)):
            correct = arr[i]
            if (arr[i] < len(arr) and arr[i] != arr[correct]):
                self.swap(arr,i,arr[i])
            else:
                i += 1
        return arr

    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
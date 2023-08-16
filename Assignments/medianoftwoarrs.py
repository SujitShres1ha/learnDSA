class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 > length2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        realmid = (length1 + length2 + 1) // 2
        start = 0
        end = length1
        
        while start <= end:
            mid = (start + end) // 2
            left1size = mid
            left2size = realmid - left1size
            
            left1 = nums1[left1size - 1] if left1size > 0 else float('-inf')
            left2 = nums2[left2size - 1] if left2size > 0 else float('-inf')
            right1 = nums1[left1size] if left1size < length1 else float('inf')
            right2 = nums2[left2size] if left2size < length2 else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if (length1 + length2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return max(left1, left2)
            elif left1 > right2:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if nums[l] < nums[r]: # because we always branch non-sorted, if it's already sorted, then that's it
                return nums[l]
            m = (l + r) // 2
            
            if nums[m] > nums[r]: # min is always in the non-sorted branch, keep branching
                l = m + 1 # go to the other branch
            else: # this is the sorted branch
                r = m

        return nums[l]
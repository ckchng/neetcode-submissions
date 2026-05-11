class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find target
        # if doesnt exists, return -1

        # key idea: always compare in the sorted side

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            # first, find out which part is sorted? 
            if nums[l] <= nums[m] <= nums[r]:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] >= nums[l]: 
                # but check if target exists in the right hand side, if it's not, we chop it
                if target >= nums[l] and target <= nums[m]: 
                    r = m - 1
                else: 
                    l = m + 1
            else: # we check the right branch
                if target >= nums[m] and target <= nums[r]: 
                    l = m + 1
                else: 
                    r = m - 1

        
        if nums[l] == target:
            return l
        else:
            return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2 
            if nums[m] == target:
                return m
            # we want to search in the sorted side
            if nums[m] >= nums[l]:
                # then this is sorted, compare here
                if target >= nums[l] and target <= nums[m]:
                    # then retain this branch
                    r = m
                else:
                    # then prune this branch
                    l = m + 1
            elif nums[r] >= nums[m]:
                # else this is sorted, search here
                if target >= nums[m] and target <= nums[r]:
                    # then keep this branch
                    l = m + 1
                else:
                    r = m


        return -1
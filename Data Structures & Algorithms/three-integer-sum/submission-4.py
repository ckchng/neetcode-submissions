class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all triplet combinations that sums up to 0
        # use dfs to collect all combinations
        res = set()
        nums.sort()

        for n_id, n in enumerate(nums):
            l = n_id + 1
            r = len(nums) - 1
            remaining = n
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum + remaining == 0:
                    res.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum + remaining > 0:
                    ## too large, move
                    r -= 1
                elif curr_sum + remaining < 0:
                    l += 1
                
    
        return list(res)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # the houses are arranged in a circle, i.e., the first and the last houses are connected
        # you either remove the last house or the first house from consideration
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def helper(nums):
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr = max(prev2 + nums[i], prev1)
                prev2, prev1 = prev1, curr
            
            return prev1
        
        return max(helper(nums[1:]), helper(nums[0:-1]))
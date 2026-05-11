class Solution:
    def rob(self, nums: List[int]) -> int:
        # you only look at the last two, just keep two running variables, no need the whole array
        if len(nums) == 1:
            return nums[0]
        
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr
        
        return prev1

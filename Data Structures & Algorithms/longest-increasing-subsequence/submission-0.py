class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # start from behind
        # use a dp to store the number of strictly larger behind nums[i]
        dp = [1] * len(nums) # base case, and setup the state vector
 
        for n_id, n in enumerate(nums):
            for prev_id in range(n_id):
                if nums[prev_id] < n:
                    tmp = dp[prev_id] + 1 # + 1 for the latest number 
                    dp[n_id] = max(tmp, dp[n_id]) # recurrence relationship, we want the max 

        return max(dp)
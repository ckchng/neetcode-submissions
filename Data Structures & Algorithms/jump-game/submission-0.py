class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = nums[0]
        for n_id in range(1, len(nums)):
            max_len -= 1
            if max_len < 0:
                return False

            max_len = max(max_len, nums[n_id])
            
            if max_len >= len(nums) - n_id:
                return True
        if len(nums) == 1:
            return max_len >= 0
        
        return True
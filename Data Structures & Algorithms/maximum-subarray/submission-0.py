class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        global_max = max_so_far
        for n_id in range(1, len(nums)):
            max_so_far = max(nums[n_id] , max_so_far + nums[n_id])
            global_max = max(max_so_far, global_max)

        return global_max
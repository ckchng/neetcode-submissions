class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track of a global max
        # keep track of max_so_far and min_so_far (the combo chain)
        # this is to handle negative numbers and 0
        global_max = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            tmp_max = max(curr, max(curr * max_so_far, curr * min_so_far))
            min_so_far = min(curr, min(curr * max_so_far, curr * min_so_far))

            global_max = max(global_max, tmp_max)
            max_so_far = tmp_max

        return global_max
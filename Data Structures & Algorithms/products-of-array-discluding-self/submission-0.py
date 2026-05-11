class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [0] * len(nums)
        from_left[0] = nums[0]
        from_right = [0] * len(nums)
        from_right[-1] = nums[-1]

        for i in range(1, len(nums)):
            from_left[i] = from_left[i-1] * nums[i]
            
        for i in range(len(nums) - 2, -1, -1):
            from_right[i] = from_right[i + 1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                nums[i] = from_right[i+1]
            elif i == len(nums) - 1:
                nums[i] = from_left[i-1]
            else:
                nums[i] = from_left[i-1] * from_right[i+1]

        return nums
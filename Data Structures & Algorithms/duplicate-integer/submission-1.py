class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = set(nums)
        if len(tab) < len(nums):
            return True
        else:
            return False
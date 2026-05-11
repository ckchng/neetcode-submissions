class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_tab = set(nums)
        return len(hash_tab) != len(nums)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab = {}
        for id, num in enumerate(nums):
            diff = target - num
            if diff in tab:
                return [tab[diff], id]
            tab[num] = id

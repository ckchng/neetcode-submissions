class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hash it
        num_hash = {}
        for id, num in enumerate(numbers):
            if num in num_hash:
                return [num_hash[num], id]
            num_hash[target - num] = id
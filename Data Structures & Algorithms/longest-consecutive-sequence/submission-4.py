class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # hash it
        tab = set(nums)
        max_length = 1
        for num in tab:
            if num - 1 not in tab:
                length = 1
                while length < len(tab):
                    if num + length in tab:
                        length += 1
                        max_length = max(length, max_length)
                    else:
                        break


        return max_length
    
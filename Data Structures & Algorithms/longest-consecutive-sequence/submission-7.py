class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we hash the numbers
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        # then we iterate the numbers, if num - 1 exists in, 
        longest_seq = 1
        for n in nums:
            if n - 1 not in nums_set:
                next_n = n + 1
                counter = 1

                while next_n in nums_set:
                    counter += 1
                    if counter > longest_seq:
                        longest_seq = counter

                    next_n = next_n + 1
                
        return longest_seq
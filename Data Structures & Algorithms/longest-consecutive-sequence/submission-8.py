class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  hash them
        seen = set(nums)
        
        max_len = 0
        for i in seen:
            curr_len = 1
            if i - 1 not in seen:
                while i + 1 in seen:
                    curr_len += 1
                    i += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l and r pointer
        # create a hash of character and position
        # if repeated, move l to position +1
        hash_map = defaultdict()
        if len(s) == 0:
            return 0
        l = 0
        hash_map[s[l]] = l
        r = 1
        max_len = 0
        while l < r and r < len(s):
            if s[r] in hash_map and hash_map[s[r]] >= l:
                l = hash_map[s[r]] + 1
            
            hash_map[s[r]] = r
            max_len = max(r - l, max_len)
            r += 1
            

        return max_len + 1
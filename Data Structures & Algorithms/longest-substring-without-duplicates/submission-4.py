class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longestLen = 1
        tab = set()

        l = 0
        r = 0

        while r < len(s):
            while s[r] in tab:
                tab.remove(s[l])
                l += 1
                
            tab.add(s[r])
            longestLen = max(longestLen, r - l + 1)

            r += 1
            

        return longestLen
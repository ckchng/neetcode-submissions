class Solution:
    def longestPalindrome(self, s: str) -> str:
        # keep track of max and their IDs
        # take care of both odd and even palindrome
        max_len = 0
        max_l = 0
        max_r = 0

        for cid in range(len(s)):
            for r in range(cid, cid+2):
                l = cid
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r + 1 - l > max_len:
                        max_len = r + 1 - l
                        max_l = l
                        max_r = r
                        
                    l -= 1
                    r += 1
                
        if max_len > 0:
            return s[max_l:max_r+1]
        else:
            return ""

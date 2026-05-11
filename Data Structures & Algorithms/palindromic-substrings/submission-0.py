class Solution:
    def countSubstrings(self, s: str) -> int:
        # from each center point, extend. Remember each char is a valid palindrome
        # so we expand from there. 
        palin_count = 0
        for c_id in range(len(s)):
            for r in range(c_id, c_id+2):
                l = c_id
                while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                    palin_count += 1
                    l-=1
                    r+=1
                
        return palin_count
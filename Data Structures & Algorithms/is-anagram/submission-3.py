class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in hash_s:
                hash_s[char] = hash_s[char] + 1
            else:
                hash_s[char] = 0
        
        for char in t:
            if char in hash_s:
                if char in hash_t:
                    hash_t[char] = hash_t[char] + 1
                else:
                    hash_t[char] = 0    
            else: 
                return False

        # iterate through the hash_s
        for char in s:
            if hash_s[char] != hash_t[char]:
                return False
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = Counter(s)
        
        for c in t:
            if c not in hash_s:
                return False
            hash_s[c] -= 1
            if hash_s[c] < 0:
                return False

        return True
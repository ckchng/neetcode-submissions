class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_tab = {}
        second_tab = {}

        if len(s) != len(t):
            return False
        for c in s:
            if c not in first_tab:
                first_tab[c] = 0
            else:
                first_tab[c] += 1
        
        for c in t:
            if c not in second_tab:
                second_tab[c] = 0
            else:
                second_tab[c] += 1
        
        for key in first_tab:
            if key not in second_tab:
                return False
            if first_tab[key] != second_tab[key]:
                return False
                
        return True
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        tab = {}
        r = 1
        l = 0
        tab[s[l]] = 1
        most_freq = 1
        res = 1
        while r < len(s):
            # update most_freq
            if s[r] not in tab:
                tab[s[r]] = 1
            else:
                tab[s[r]] += 1
                if tab[s[r]] > most_freq:
                    most_freq = tab[s[r]]

            if (r - l + 1) - most_freq > k:
                # update l
                # update table
                # l+=1
                tab[s[l]] -= 1 # this is neccesary 
                l+=1

            res = max(res, r - l + 1)
                        
            r += 1

        return res
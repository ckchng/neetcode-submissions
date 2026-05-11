class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hash t
        s_tab = {}
        t_tab = {}
        # maintain a min_len
        min_len = float("infinity")
    
        for c in t:
            if c not in t_tab:
                t_tab[c] = 1
            else:
                t_tab[c] += 1
    
        
        l = 0
        r = 0
        # maintain two counters, have and need
        have = 0
        need = len(set(t))
        best_window = [l, r]
        while r < len(s):
            # expand the window in s
            if s[r] not in s_tab:
                s_tab[s[r]] = 1
            else:
                s_tab[s[r]] += 1
            
            if s[r] in t_tab and s_tab[s[r]] == t_tab[s[r]]:
                have += 1
            
            if have == need:
                # shrink the window if possible
                while l < r:
                    if s[l] in t_tab:
                        if s_tab[s[l]] == t_tab[s[l]]: # stop when the left most in s_tab has the same value as t_tab    
                            break
                    
                    if (s[l] in t_tab and s_tab[s[l]] > t_tab[s[l]]) or s[l] not in t_tab:
                        s_tab[s[l]] = max(0, s_tab[s[l]] - 1)
                    
                    l+=1

            if have == need and (r - l + 1 < min_len):
                # update min len
                min_len = r - l + 1
                best_window = [l, r]

            r += 1
                

        if min_len >= need and min_len != float("infinity"):
            return s[best_window[0]:best_window[1]+1]
        else:
            return "" 
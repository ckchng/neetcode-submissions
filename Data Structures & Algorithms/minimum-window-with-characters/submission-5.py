class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_tab = {}
        s_tab = {}
        have = 0
        need = len(set(t))
        for c in t:
            if c not in t_tab:
                t_tab[c] = 1
            else:
                t_tab[c] += 1

        l = 0
        r = 0
        best_window = [l, r]
        shortest_len = float("infinity")
        # expanding operation
        while r < len(s):
            # add current c into s_tab
            if s[r] not in s_tab:
                s_tab[s[r]] = 1
            else:
                s_tab[s[r]] += 1

            # only add one time to the have counter
            if s[r] in t_tab and s_tab[s[r]] == t_tab[s[r]]:
            # if s[r] in t_tab:
                have += 1

            r += 1

            # shrinking operation
            if have == need:
                # try to remove s[l] in t_tab, if we cant, then that's it
                while l < r:
                    if (s[l] in t_tab and s_tab[s[l]] > t_tab[s[l]]) or s[l] not in t_tab:
                        s_tab[s[l]] -= 1
                        l+=1
                    elif s_tab[s[l]] == t_tab[s[l]]:
                        break
                
                window_len = r - l + 1
                if window_len < shortest_len:
                    best_window = [l, r]
                    shortest_len = window_len
                
                # remove the leftmost char
                s_tab[s[l]] = max(s_tab[s[l]] - 1, 0)
                l += 1
                have -= 1
                
        if shortest_len != float("infinity"):
            return s[best_window[0]:best_window[1]]
        else:
            return ""

        
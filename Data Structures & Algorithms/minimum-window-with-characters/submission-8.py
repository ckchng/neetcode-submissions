class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build a hash for t

        # use a sliding window approach to go thru s

        # expand the window to find all the matches in hash t with the correct frequency

        # when it doesnt include t, move l. So s[l] always contains the any character in t

        # It's ok to have duplicate, so the frequency can be >=
        # when all is found, update min_len, move l to the first position + 1 (how)

        # build a hash for s. key: char, val: freq, position. We will need to go through all positions.
        
        hash_t = Counter(t)
        unique_t = len(set(t))
        formed = 0
        l = 0
        min_len = len(s) + 1
        min_l = 0
        min_r = 0
        window_hash = {}
        # if sum == len(t): update form as soon as the frequency is matched
        # do we need another hash?
        for r in range(len(s)):            
            window_hash[s[r]] = window_hash.get(s[r], 0) + 1

            if s[r] in hash_t:
                if window_hash[s[r]] == hash_t[s[r]]:
                    formed += 1
            
            # check if we have everything that we need
            # if formed == len(t):
                # shrink window by moving up the left pointer
            while formed == unique_t and l <= r:
                
                if r + 1 - l < min_len:
                    min_len = r + 1 - l
                    min_l = l
                    min_r = r
                window_hash[s[l]] -= 1

                if s[l] in hash_t:
                    if window_hash[s[l]] < hash_t[s[l]]:
                        formed -= 1

                l += 1
                
            r+= 1
            

        if min_len == len(s) + 1:
            return ""
        else:
            return s[min_l:min_r+1]
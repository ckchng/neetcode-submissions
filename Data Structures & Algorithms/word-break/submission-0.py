class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use the dp approach
        # the formula for bottom up is dp[i] = d[i + len(w)]
        # each [i] indicate is if possible to find a word in wordDict starting from i

        
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

                    if dp[i]:
                        break

        return dp[0]       
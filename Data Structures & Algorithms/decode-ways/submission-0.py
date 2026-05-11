class Solution:
    def numDecodings(self, s: str) -> int:
        # create a dp with len(s) + 1
        # dp[i] represents the number of ways at i-th char, indexed by i-1
        # otherwise, ways[i] = ways[i-1]
        # ways[i] = ways[i-1] + ways[i-2] # if it's a legit conversion

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        if s[0] != '0':
            dp[1] = dp[0] 
        
        for i in range(2, len(s) + 1):
            if int(s[i - 1]) != 0:
                dp[i] = dp[i - 1]
            
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
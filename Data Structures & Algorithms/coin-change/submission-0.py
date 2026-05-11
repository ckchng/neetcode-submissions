class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we need a global solution. Unless you can set a lb for your best first search, otherwise, it wont work.
        #
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1): 
            # for each potential discrete value, # find out the minimum number of combinations from the coins
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
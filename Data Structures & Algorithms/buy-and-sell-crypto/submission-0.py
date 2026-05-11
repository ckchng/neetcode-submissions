class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the minimum
        # compute profit on each day
        min_price = prices[0]
        max_profit = 0
        for p_id in range(1, len(prices)):
            max_profit = max(max_profit, prices[p_id] - min_price)
            if prices[p_id] < min_price:
                min_price = prices[p_id]

        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0
        for price in prices:
            min_so_far = min(min_so_far, price)
            profit = price - min_so_far
            max_profit = max(profit, max_profit)
        return max_profit
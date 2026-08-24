class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profitMax = 0
        r = 0

        while r < len(prices):
            if prices[left] < prices[r]:
                profit = prices[r] - prices[left]
                profitMax = max(profitMax, profit)
            else:
                left = r
            r +=1
        return profitMax
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profitMax = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                profitMax = max(profitMax, profit)
            else:
                left = right
            right +=1
        return profitMax
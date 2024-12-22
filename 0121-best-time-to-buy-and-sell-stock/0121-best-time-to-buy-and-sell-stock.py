class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit: int = 0

        if not prices: return 0

        minPrice = prices[0]

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else: profit = max(profit, prices[i] - minPrice)

        return profit


        


        
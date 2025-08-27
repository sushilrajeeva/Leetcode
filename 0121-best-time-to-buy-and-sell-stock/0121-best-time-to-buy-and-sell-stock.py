class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            price = prices[i]
            if minPrice > price:
                minPrice = price
            else:
                profit = max(profit, price - minPrice)

        return profit
        
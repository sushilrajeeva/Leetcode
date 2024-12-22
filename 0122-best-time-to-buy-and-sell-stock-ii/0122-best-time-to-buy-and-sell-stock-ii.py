class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit: int = 0
        minPrice = float("inf")

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                profit += (prices[i] - minPrice)
                minPrice = prices[i]

        return profit

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        minPrice = float("inf")
        for i in range(n):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                result += prices[i] - minPrice
                minPrice = prices[i]

        return result
        
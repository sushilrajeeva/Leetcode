class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit: int = 0
        n: int = len(prices)

        if n <= 1:
            return 0

        prev = prices[0]
        for i in range(n):
            profit = max(profit, prices[i]-prev)
            prev = min(prev, prices[i])

        return profit


        


        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float("inf")
        buy2 = float("inf")

        sell1 = 0
        sell2 = 0

        n = len(prices)

        for i in range(n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)

        return sell2
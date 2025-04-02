class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if cur > prices[i]:
                cur = prices[i]
            else:
                profit = max(profit, prices[i] - cur)
        return profit

        
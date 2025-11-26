from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices[:]
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] -= prices[i]

            stack.append(i)

        return ans
      

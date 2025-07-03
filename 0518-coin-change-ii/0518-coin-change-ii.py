from collections import *
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n: int = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n)]

        def numberOfWays(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == n:
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]
            
            if coins[i] > amount:
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)

            return memo[i][amount]

        

        res = numberOfWays(0, amount)
        print("memo", memo)
        return res
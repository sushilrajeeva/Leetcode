class Solution:

    """
        are coins +ve ? true
        same signature i.e 1, 2, 2 == 2, 1, 2 == 2, 2, 1
        amount range = 0 <= amount <= 5000
        edge case is how many ways to make amount 0 ? 1 way


        Algo:

            TC: 2^N * AMOUNT
            SC = O(HEIGHT) (RECURISON DEPTH)

            count_ways(index, remaining_amount):
                if remaining_amount == 0:
                    return 1
                if remaining_amount < 0 or index ==len(coins):
                    return 0
                
                # option 1 - include coins[index]
                include = count_ways(index, remanining_amount - coins[index])

                # Option 2 - exclude
                exclude = count_ways(index + 1, remaining_amount)

                return include + exclude

            return count_ways(0, amount)

        Algo Optimal:
            def code(amount, coins):
                dp = array of size (amount + 1) and initialize all to 0
                dp[0] = 1

                for each coin in coins:
                    for i from coin to amount:
                        dp[i] += dp[i - coin]

                return dp[amount]


                amount = 5 coins = [1, 2, 5]
                dp = [1, 0, 0, 0, 0, 0]

                coin = 1:
                    i = 1 dp[1] = dp[1] + dp[0] = 1
                    i = 2 dp[2] = dp[2] + dp[1] = 1
                    i = 3 dp[3] = dp[3] + dp[2] = 1
                    i = 4 dp[4] = 1
                    i = 5 dp[5] = 1

                dp = [1, 1, 1, 1, 1, 1]

                coin = 2
                    i = 2 dp[2] = dp[2] + dp[0] = 1 + 1 = 2
                    i = 3 dp[3] = dp[3] + dp[1] = 1 + 1 = 2
                    i = 4 dp[4] = dp[4] + dp[2] = 1 + 2 = 3
                    i = 5 dp[5] = dp[5] + dp[3] = 1 + 2 = 3
                dp = [1, 1, 2, 2, 3, 3]

                coin = 5
                    i = 5 dp[5] = dp[5] + dp[0] = 3 + 1 = 4
                dp = [1, 2, 2, 3, 4]

                returning dp[5] = 4 

    """

    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)

        dp [0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i-coin]

        return dp[amount]
        
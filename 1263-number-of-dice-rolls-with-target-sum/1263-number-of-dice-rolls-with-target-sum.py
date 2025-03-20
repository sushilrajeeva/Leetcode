class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Comment: We define the modulo constant
        MOD = 10**9 + 7
        
        # Comment: Create a 2D DP array
        # dp[i][j] will store the number of ways to get sum j with i dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Comment: Base case
        # With 0 dice, there's exactly 1 way to get sum 0 (by choosing nothing)
        dp[0][0] = 1
        
        # Comment: Fill the DP table
        # Outer loop for the number of dice
        for dice_count in range(1, n + 1):
            # Inner loop for all possible sums up to target
            for current_sum in range(1, target + 1):
                # We sum over all possible face values (1 through k)
                # but ensure we don't go below 0 for the index
                ways = 0
                for face_value in range(1, k + 1):
                    if current_sum - face_value >= 0:
                        ways += dp[dice_count - 1][current_sum - face_value]
                # Take modulo to avoid large numbers
                dp[dice_count][current_sum] = ways % MOD
        
        # Comment: Return the number of ways to get 'target' with 'n' dice
        return dp[n][target] % MOD
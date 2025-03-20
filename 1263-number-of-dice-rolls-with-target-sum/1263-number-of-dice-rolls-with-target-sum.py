class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Define the modulo constant to keep numbers manageable
        MOD = 10**9 + 7
        
        # Create a dictionary to memoize the results for (dice, remaining) state
        memo = {}
        
        # Define the recursive function for DFS with memoization
        def dfs(dice, remaining):
            # Base Case 1: When no dice left and remaining sum is 0, it's a valid solution.
            if dice == 0 and remaining == 0:
                return 1
            # Base Case 2: If no dice left or remaining sum is negative, it's invalid.
            if dice == 0 or remaining < 0:
                return 0
            
            # If the result for this state is already computed, return it.
            if (dice, remaining) in memo:
                return memo[(dice, remaining)]
            
            # Initialize ways to count the number of valid combinations for this state.
            ways = 0
            # Try each face value from 1 to k
            for face in range(1, k + 1):
                # Recursively compute the number of ways by reducing one die and the remaining sum
                ways += dfs(dice - 1, remaining - face)
                # Apply modulo after each addition to avoid large numbers
                ways %= MOD
            
            # Store the computed result in memoization dictionary
            memo[(dice, remaining)] = ways
            return ways
        
        # Call the recursive function starting with n dice and the target sum.
        return dfs(n, target)

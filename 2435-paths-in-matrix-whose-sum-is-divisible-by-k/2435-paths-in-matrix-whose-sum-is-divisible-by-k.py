class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        m: int = len(grid)
        n: int = len(grid[0])

        MOD = 10 ** 9 + 7

        memo = {}

        def recursion(row: int, col: int, rem: int) -> None:

            if row >= m or col >= n:
                return 0
            
            
            new_rem = (rem + grid[row][col]) % k

            if row == m - 1 and col == n - 1:
                return 1 if new_rem == 0 else 0

            key = (row, col, new_rem)
            if key in memo:
                return memo[key]

            total_path = (recursion(row + 1, col, new_rem) + recursion(row, col + 1, new_rem)) % MOD

            memo[key] = total_path
            return memo[key]


        return recursion(0, 0, 0)

        
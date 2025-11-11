class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Fixed initialization

        for s in strs:
            countList = self.countZeroesOnes(s)
            zeros_needed, ones_needed = countList[0], countList[1]
            # Iterate backwards from m to zeros_needed (inclusive)
            for zeros in range(m, zeros_needed - 1, -1):
                for ones in range(n, ones_needed - 1, -1):
                    dp[zeros][ones] = max(
                        1 + dp[zeros - zeros_needed][ones - ones_needed],
                        dp[zeros][ones]
                    )
        return dp[m][n]

    def countZeroesOnes(self, s: str) -> List[int]:
        c = [0, 0]
        for char in s:  # Iterate over characters directly
            if char == '0':
                c[0] += 1
            else:
                c[1] += 1
        return c
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        dp = [0] * (n)
        maximum = float("-inf")
        for i in reversed(range(n)):
            if i + k < n:
                dp[i] = dp[i + k] + energy[i]
            else:
                dp[i] = energy[i]
            maximum = max(maximum, dp[i])

        return maximum
        
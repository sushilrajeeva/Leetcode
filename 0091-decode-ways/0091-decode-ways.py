class Solution:
    def numDecodings(self, s: str) -> int:

        # get length of the string
        n: int = len(s)

        if n == 0: return 0

        if s[0] == '0': return 0

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        

        for i in range(2, n+1):
            cur: str = s[i-1]
            if cur != '0':
                dp[i] += dp[i-1]

            prev: str = s[i-2]

            twoDigit: int = int(prev) * 10 + int(cur)

            if 10 <= twoDigit <= 26:
                dp[i] += dp[i-2]

        return dp[n]
            

        
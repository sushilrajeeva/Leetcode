class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n: int = len(days)
        memo = {}

        def dp(i: int) -> int:

            if i >= n: return 0

            if i in memo:
                return memo[i]

            # purchase 1 day ticket
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            cost1 = costs[0] + dp(j)

            # purchase 7 days ticket
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            cost2 = costs[1] + dp(j)

            # purchase 30 days ticket
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            cost3 = costs[2] + dp(j)

            memo[i] = min(cost1, cost2, cost3)
            return memo[i]


        return dp(0)

            
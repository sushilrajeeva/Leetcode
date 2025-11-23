class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        for n in reversed(range(len(costs)-1)):
            for color in range(len(costs[n])):
                costs[n][color] += min([costs[n+1][x] for x in range(len(costs[n+1])) if x!=color])

        return min(costs[0])
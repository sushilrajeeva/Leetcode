from typing import *
from collections import defaultdict

# OVERALL:
    # TC = O(N)
    # SC = O(N)
class Solution:

    # TC: O(N)
    # SC: O(N)
    def build_graph(self, roads: List[List[int]]) -> Dict[int, List[int]]:
        self.graph = defaultdict(list)
        for u, v in roads:
            self.graph[u].append(v)
            self.graph[v].append(u)
        return self.graph


    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph: Dict[int, List[int]] = self.build_graph(roads)

        self.fuel = 0
        # TC: O(V+E) => O(N) + O(N -1) => O(2N-1) = O(N)
        # SC: O(V) => O(N)
        def dfs(node: int, parent: int) -> int:
            reps = 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                other_reps = dfs(neighbor, node)
                self.fuel += math.ceil(other_reps/seats)
                reps += other_reps

            return reps

        dfs(0, -1)

        return self.fuel
        
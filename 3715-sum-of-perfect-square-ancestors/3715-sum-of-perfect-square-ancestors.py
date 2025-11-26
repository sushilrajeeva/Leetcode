from collections import defaultdict
class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def square_free(x: int) -> int:
            i = 2
            while i * i <= x:
                count = 0
                while x % i == 0:
                    x //= i
                    count ^= 1
                if count == 1:
                    x *= i
                i += 1
            return x

        sq = [square_free(v) for v in nums]

        ans = 0
        count = defaultdict(int)
        def dfs(node: int, parent: int):
            nonlocal ans
            val = sq[node]
            ans += count[val]

            count[val] += 1

            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
            count[val] -= 1

        dfs(0, -1)
        return ans
        
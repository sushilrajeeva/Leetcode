class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n: int = len(isConnected)
        visited: List[bool] = [False] * n

        def dfs(node: int):
            visited[node] = True
            for neighbor in range(n):
                if not visited[neighbor] and isConnected[node][neighbor] == 1:
                    dfs(neighbor)
        
        count: int = 0

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count
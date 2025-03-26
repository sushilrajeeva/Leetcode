class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n: int = len(isConnected)
        visited: List[bool] = [False] * n

        def dfs(node: int) -> None:
            if not visited[node]:
                visited[node] = True
                for neighbor in range(n):
                    if not visited[neighbor] and isConnected[node][neighbor] == 1:
                        dfs(neighbor)

        count: int = 0
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count          
        
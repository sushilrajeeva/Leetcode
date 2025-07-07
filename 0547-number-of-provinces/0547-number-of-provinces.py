class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n: int = len(isConnected) # no of cities
        visited: List[bool] = [False] * n

        def dfs(node: int) -> None:
            visited[node] = True

            for i in range(n):
                if not visited[i] and isConnected[node][i] == 1:
                    dfs(i)

        count: int = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
                
        return count



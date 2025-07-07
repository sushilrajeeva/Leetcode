class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n: int = len(isConnected)
        m: int = len(isConnected[0])
        visited: List[bool] = [False] * n
        count: int = 0

        def dfs(node: int) -> None:
            if visited[node]: return
            visited[node] = True
            for i in range(n):
                if not visited[i] and isConnected[node][i] == 1:
                    dfs(i)


        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

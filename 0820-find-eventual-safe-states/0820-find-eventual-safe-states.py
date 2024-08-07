class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        visited = [False] * n
        pathVisited = [False] * n

        seq = [False] * n

        def dfs(node: int) -> bool:
            if not visited[node]:
                visited[node] = True
                pathVisited[node] = True

                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True

                seq[node] = True
            elif visited[node] and pathVisited[node]: return True

            pathVisited[node] = False

            return False

        for i in range(n):
            if not visited[i]:
                dfs(i)

        return [index for index, value in enumerate(seq) if value == True]
                
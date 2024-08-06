from queue import Queue

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
       
        def dfs(node: int, color: int):

            if colors[node] == -1:
                colors[node] = color
                color = 1 if color == 0 else 0
                
                for v in graph[node]:
                    if not dfs(v, color):
                        return False
            elif colors[node] != color:
                return False

            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

        

                
            



        
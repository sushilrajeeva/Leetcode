from queue import Queue

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)

        color = [-1] * n # can replace it with 0 or 1 for color

        for start in range(n):
            if color[start] == -1:  # Only start BFS if the node is uncolored
                color[start] = 0
                q = Queue()
                q.put(start)

                while not q.empty():
                    node = q.get()
                    c = 1 if color[node] == 0 else 0

                    for v in graph[node]:
                        if color[v] == -1:
                            color[v] = c
                            q.put(v)
                        elif color[v] == color[node]:
                            return False

        return True
                
            



        
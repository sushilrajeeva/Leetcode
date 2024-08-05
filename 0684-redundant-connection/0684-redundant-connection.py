class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        visited = [False] * (n+1)

        adj = [[] for _ in range(n+1)]


    
        def dfs(node, parent):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if dfs(neighbor, node):
                        return True
                elif visited[neighbor] and neighbor != parent: return True

            return None

        for edge in edges:
            visited = [False] * (n+1)

            e1, e2 = edge[0], edge[1]

            adj[e1].append(e2)
            adj[e2].append(e1)

            if dfs(e1, -1):
                return [e1, e2]

        return []
                        
        
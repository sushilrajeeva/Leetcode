class Solution:

    def build_adj_list(self,n, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build an undirected graph
        adj: List[List[int]] = self.build_adj_list(n, edges)
        
        visited = [False] * n
        
        def dfs(node: int, component: Set[int]):
            """Perform DFS to collect nodes in the connected component."""
            visited[node] = True
            component.add(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        def isComplete(component: Set[int]) -> bool:
            """Check if the given component is complete."""
            k = len(component)
            # A single node is complete by definition
            if k == 1:
                return True
            # Count the number of edges in this component.
            edge_count = 0
            for node in component:
                # Only count neighbors that are in the component
                for neighbor in adj[node]:
                    if neighbor in component:
                        edge_count += 1
            # In an undirected graph, each edge is counted twice.
            edge_count //= 2
            return edge_count == k * (k - 1) // 2
        
        complete_components = 0
        for i in range(n):
            if not visited[i]:
                component = set()
                dfs(i, component)
                if isComplete(component):
                    complete_components += 1
        
        return complete_components

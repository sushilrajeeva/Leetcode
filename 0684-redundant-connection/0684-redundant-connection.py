class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper function to find the root of a node
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        # Helper function to union two nodes
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root2] = root1
                return False
            return True  # Cycle detected

        # Initialize parent array for each node
        n = len(edges)
        parent = [i for i in range(n + 1)]  # Using 1-based index

        # Process each edge
        for node1, node2 in edges:
            if union(node1, node2):
                return [node1, node2]

        return []
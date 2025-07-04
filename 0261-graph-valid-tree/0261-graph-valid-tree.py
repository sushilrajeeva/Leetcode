class Solution:

    def build_adjacency_list(self, edges: List[List[int]]) -> Dict[int, set[int]]:
        graph: Dict[int, set[int]] = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        return graph


    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Quick check: a tree on n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        visited: Set[int] = set()


        graph: Dict[int, set[int]] = self.build_adjacency_list(edges)

        def visit(node: int, parent: int) -> None:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited: return False
                if not visit(neighbor, node): return False
            return True
        visit(0, -1)

        return len(visited) == n

        
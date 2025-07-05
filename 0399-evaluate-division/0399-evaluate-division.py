class Solution:

    def build_graph(self, equations: List[List[str]], values: List[float]) -> Dict[str, List[Tuple[str, float]]]:
        graph: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        n: int = len(equations)

        for i in range(n):
            source: str = equations[i][0]
            destination: str = equations[i][1]
            rate: int = values[i]
            graph[source].append((destination, rate))
            graph[destination].append((source, (1.0/rate)))
        return graph


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph: Dict[str, List[Tuple[str, int]]] = self.build_graph(equations, values)
        results: List[float] = []

        def dfs(source: str, destination: str, value: float, visited: Set[str]) -> float:
            if source == destination:
                return value
            visited.add(source)
            for currency, rate in graph[source]:
                if currency in visited:
                    continue
                else:
                    res = dfs(currency, destination, rate * value, visited)
                    if res != -1.0:
                        return res
            return -1.0

        for src, dst in queries:
            if src not in graph or dst not in graph:
                results.append(-1.0)
            else:
                visited: Set[str] = set()
                result = dfs(src, dst, 1.0, visited)
                results.append(result)

        return results
        
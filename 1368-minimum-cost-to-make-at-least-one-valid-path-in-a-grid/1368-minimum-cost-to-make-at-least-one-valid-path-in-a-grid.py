class Solution:
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        cost = 0

        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]

        queue = collections.deque()

        self._dfs(grid, 0, 0, min_cost, cost, queue)

        while queue:
            cost += 1
            level_size = len(queue)

            for _ in range(level_size):
                row, col = queue.popleft()
                for dir_idx, (dx, dy) in enumerate(self._dirs):
                    self._dfs(grid, row + dx, col + dy, min_cost, cost, queue)

        return min_cost[num_rows - 1][num_cols - 1]
    def _dfs(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        min_cost: List[List[int]],
        cost: int,
        queue: collections.deque,
    ) -> None:
        if not self._is_unvisited(min_cost, row, col):
            return

        min_cost[row][col] = cost
        queue.append((row, col))

        next_dir = grid[row][col] - 1
        dx, dy = self._dirs[next_dir]
        self._dfs(grid, row + dx, col + dy, min_cost, cost, queue)

    def _is_unvisited(
        self, min_cost: List[List[int]], row: int, col: int
    ) -> bool:
        return (
            0 <= row < len(min_cost)
            and 0 <= col < len(min_cost[0])
            and min_cost[row][col] == float("inf")
        )
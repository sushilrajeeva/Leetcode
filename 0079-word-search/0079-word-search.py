class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R: int = len(board)
        C: int = len(board[0])

        visited: List[List[bool]] = [[False] * C for _ in range(R)]
        directions: Tuple[Tuple[int, int]] = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def isValid(r: int, c: int) -> bool:
            return 0 <= r < R and 0 <= c < C

        def dfs(r: int, c: int, i) -> bool:
            # 1) Out of bounds or wrong letter or already used?
            if not isValid(r, c) or visited[r][c] or board[r][c] != word[i]:
                return False

            # 2) If it is the last letter of the word, we are done
            if i == len(word) - 1:
                return True
            
            # exploring all the directions
            visited[r][c] = True
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            # backtracking
            visited[r][c] = False
            return False

        # Try each cell
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False
        
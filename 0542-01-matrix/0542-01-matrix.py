from queue import Queue

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])

        visited = [[False] * m for _ in range(n)]

        dist = [[0] * m for _ in range(n)]

        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = Queue()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.put((i, j, 0))
                    visited[i][j] = True
        
        while not q.empty():
            row, col, distance = q.get()
            dist[row][col] = distance

            for r, c in directions:
                newRow, newCol = row + r, col + c

                if 0 <= newRow < n and 0 <= newCol < m and not visited[newRow][newCol]:
                    visited[newRow][newCol] = True
                    q.put((newRow, newCol, distance+1))

        
        return dist


        
import heapq

class Solution:
    def findShortestWay(self, maze, ball, hole):
        m, n = len(maze), len(maze[0])
        q = [(0, "", ball[0], ball[1])]
        stopped = {(ball[0], ball[1]): [0, ""]}

        while q:
            dist, pattern, x, y = heapq.heappop(q)

            # If we've reached the hole with the best (dist, pattern), return it
            if [x, y] == hole:
                return pattern

            # Try all four directions
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"),
                            (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0

                # Roll until wall or hole
                while (0 <= newX + i < m and 0 <= newY + j < n and
                       maze[newX + i][newY + j] != 1):
                    newX += i
                    newY += j
                    d += 1
                    if [newX, newY] == hole:
                        break

                # Check if this stopping point is better than what we had
                if ((newX, newY) not in stopped or
                    [dist + d, pattern + p] < stopped[(newX, newY)]):

                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))

        return "impossible"

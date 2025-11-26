class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        grid = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for i, j in product(range(m-2), range(n-2)):
            s = 0
            for ii, jj in product(range(i, i+3), range(j, j+3)):
                if (ii < i+2 and abs(image[ii+1][jj] - image[ii][jj]) > threshold or 
                    jj < j+2 and abs(image[ii][jj+1] - image[ii][jj]) > threshold):
                    break
                s += image[ii][jj]
            else:
                s //= 9
                for ii, jj in product(range(i, i+3), range(j, j+3)):
                    grid[ii][jj][0] += s
                    grid[ii][jj][1] += 1

        for i, j in product(range(m), range(n)):
            if grid[i][j][1]:
                image[i][j] = grid[i][j][0] // grid[i][j][1]
        return image
import java.util.LinkedList;
import java.util.Queue;

class Data {
    Integer row;
    Integer col;
    Integer time;

    public Data(Integer row, Integer col, Integer time) {
        this.row = row;
        this.col = col;
        this.time = time;
    }
}

class Solution {
    public int orangesRotting(int[][] grid) {

        Queue<Data> queue = new LinkedList<>();
        int n = grid.length;
        int m = grid[0].length;
        int freshCount = 0;
        int maxTime = 0;

        int [][] directions = {
            {-1, 0}, // up
            {1, 0}, // down
            {0, -1}, // left
            {0, 1} // right
        };

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(grid[i][j] == 2) {
                    queue.add(new Data(i, j, 0));
                } else if (grid[i][j] == 1) {
                    freshCount += 1;
                }
            }
        }

        while (!queue.isEmpty()) {
            Data data = queue.remove();
            int row = data.row;
            int col = data.col;
            int time = data.time;

            maxTime = Math.max(maxTime, time);

            for (int[] rc : directions) {
                int newRow = row + rc[0];
                int newCol = col + rc[1];

                if ((newRow >= 0 && newRow < n) && (newCol >= 0 && newCol < m) && grid[newRow][newCol] == 1) {
                    grid[newRow][newCol] = 2;
                    queue.add(new Data(newRow, newCol, time+1));
                    freshCount -= 1;
                }
            }

        }

        if (freshCount > 0) {
            return -1;
        }

        return maxTime;

        
        
    }
}
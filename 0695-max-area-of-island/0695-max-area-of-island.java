class Solution {

    private static final int[][] directions = new int[][] {
        {0, 1},
        {1, 0},
        {0, -1},
        {-1, 0}
    };
    
    public int maxAreaOfIsland(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;

        int max_area = 0;
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                if (grid[row][col] == 1){
                    int area = dfs(grid, row, col, rows, cols);
                    max_area = Math.max(area, max_area);
                }
            }
        }

        return max_area;
    }

    private boolean isValid(int[][] grid, int row, int col, int rows, int cols) {
        return (row >= 0 && row < rows) && (col >= 0 && col < cols);
    };

    int dfs(int[][] grid, int row, int col, int rows, int cols) {

        if (!isValid(grid, row, col, rows, cols) || grid[row][col] != 1){
            return 0;
        }

        int area = 1;
        grid[row][col] = -1;

        for (int[] direction: directions) {
            int r = direction[0] + row;
            int c = direction[1] + col;

            area += dfs(grid, r, c, rows, cols);
        }

        return area;
    };
}
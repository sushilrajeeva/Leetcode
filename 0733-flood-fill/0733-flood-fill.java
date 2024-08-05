class Solution {

    public void dfs (int sr, int sc, int[][] image, int color, int key, ArrayList<ArrayList<Integer>> visited, int n, int m) {

        if (sr < 0 || sr >= n || sc < 0 || sc >=m || image[sr][sc] != key || visited.get(sr).get(sc) == 1){
            return;
        }

        visited.get(sr).set(sc, 1);
        image[sr][sc] = color;

        dfs(sr - 1, sc, image, color, key, visited, n, m); // UP
        dfs(sr + 1, sc, image, color, key, visited, n, m); // DOWN
        dfs(sr, sc - 1, image, color, key, visited, n, m); // LEFT
        dfs(sr, sc + 1, image, color, key, visited, n, m); // RIGHT

    }

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        ArrayList<ArrayList<Integer>> visited = new ArrayList<>();
        int n = image.length;
        int m = image[0].length;

        int key = image[sr][sc];


        for (int i = 0; i < n; i++) {
            visited.add(new ArrayList<>());
            for (int j = 0; j < m; j++) {
                visited.get(i).add(0);
            }
        }

        dfs(sr, sc, image, color, key, visited, n, m);

        return image;


    }

}
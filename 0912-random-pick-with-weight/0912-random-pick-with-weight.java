class Solution {

    private ArrayList<Integer> weights = new ArrayList<>();
    public Solution(int[] w) {
        int total = 0;
        for (int weight : w) {
            total += weight;
            weights.add(total);
        }
        
    }
    
    public int pickIndex() {
        int rand = (int)(Math.random() * (weights.get(weights.size() - 1)));
        int left = 0;
        int right = weights.size() - 1;
        while (left <= right) {
            int mid = (int)((right - left) / 2 + left);
            if (rand < weights.get(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
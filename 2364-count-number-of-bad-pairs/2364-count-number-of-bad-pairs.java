class Solution {
    public long countBadPairs(int[] nums) {
        long n = nums.length;
        long totalPairs = n * (n - 1) / 2;
        long goodPairs = 0;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int key = nums[i] - i;
            // Current element forms good pairs with all previous elements having same key
            goodPairs += map.getOrDefault(key, 0);
            // Update frequency
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        
        return totalPairs - goodPairs;
    }
}
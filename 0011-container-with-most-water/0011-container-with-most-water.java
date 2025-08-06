class Solution {
    public int maxArea(int[] height) {

        int max_water = 0;
        
        int left = 0;
        int n = height.length;
        int right = n - 1;

        while (left < right) {
            int water = (right - left) * Math.min(height[left], height[right]);
            max_water = Math.max(water, max_water);
            if (height[left] < height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return max_water;
        
    }
}
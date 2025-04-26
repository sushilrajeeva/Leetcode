class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int trappedWater = 0;
        int [] leftMax = new int[n];
        int [] rightMax = new int[n];

        int tempLeft = 0;
        for (int i =0; i < n; i ++) {
            tempLeft = Math.max(tempLeft, height[i]);
            leftMax[i] = tempLeft;
        }

        int tempRight = 0;
        for (int i = n - 1; i >=0; i--) {
            tempRight = Math.max(tempRight, height[i]);
            rightMax[i] = tempRight;
        }

        for (int i = 0; i < n; i++) {
            int computation = Math.min(leftMax[i], rightMax[i]) - height[i];
            trappedWater += computation > 0 ? computation : 0;
        }

        return trappedWater;
        
    }
}
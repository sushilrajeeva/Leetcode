class Solution {
    public int trap(int[] height) {

        int n = height.length;
        if (n == 0) return 0;

        int [] prefixArr = new int[n];
        int [] suffixArr = new int[n];

        // Computing prefixArr and suffixArr
        int tempLeft = 0;
        int tempRight = 0;
        for (int i = 0; i < n; i++) {
            tempLeft = Math.max(tempLeft, height[i]);
            tempRight = Math.max(tempRight, height[n-i-1]);
            prefixArr[i] = tempLeft;
            suffixArr[n-i-1] = tempRight;
        }

        int water = 0;

        for (int i = 0; i < n; i++) {
            int computation = Math.min(prefixArr[i], suffixArr[i]) - height[i];
            water += computation > 0 ? computation : 0;
        }

        return water;

        
    }


}
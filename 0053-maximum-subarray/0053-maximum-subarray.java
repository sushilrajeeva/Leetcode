import java.lang.Math;
class Solution {
    public int maxSubArray(int[] nums) {

        int maxSeen = Integer.MIN_VALUE;
        int subMax = 0;

        for(int i = 0; i < nums.length; i++) {
            subMax += nums[i];
            if (maxSeen <= subMax) {
                maxSeen = subMax;
            } 

            if (subMax < 0) {
                subMax = 0;
            }
        }

        return maxSeen;
        
    }
}
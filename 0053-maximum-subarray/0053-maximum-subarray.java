import java.lang.Math;
class Solution {
    public int maxSubArray(int[] nums) {

        int n = nums.length;
        if(n==0){
            return 0;
        }

        int path = nums[0];
        int maxSum = nums[0];

        for(int i=1; i<nums.length; i++){
            path = Math.max(nums[i], path + nums[i]);
            maxSum = Math.max(maxSum, path);
        }

        return maxSum;
        
    }
}
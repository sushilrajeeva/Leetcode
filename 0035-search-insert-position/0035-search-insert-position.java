class Solution {
    public int searchInsert(int[] nums, int target) {

        int n = nums.length;
        int left = 0;
        int right = n - 1;

        while(left<=right){
            int mid = left - (left-right)/2;

            // if mid element is the target then return mid
            if(nums[mid] == target){
                return mid;
            }

            if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        return left;
        
    }
}
class Solution {
    public int search(int[] nums, int target) {

        int n = nums.length;
        int left = 0;
        int right = n-1;

        while(left<=right){
            int mid = left - (left - right)/2;
            
            // if mid element is the target then return index (mid)
            if(nums[mid] == target){
                return mid;
            }

            // if target is greater than mid then narrow the search space by moving left to mid + 1
            if(nums[mid] < target){
                left = mid + 1;
            }else{
                // else narrow the search space by moving right to mid - 1
                right = mid - 1;
            }
        }

        return -1;
        
    }
}
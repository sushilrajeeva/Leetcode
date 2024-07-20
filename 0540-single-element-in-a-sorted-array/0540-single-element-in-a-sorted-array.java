class Solution {
    public int singleNonDuplicate(int[] nums) {

        int n = nums.length;
        int left = 0;
        int right = n-1;

        // checking for edge cases
        if(n==1){
            return nums[0];
        }else if(nums[0] != nums[1]){
            return nums[0];
        }else if(nums[right] != nums[right-1]){
            return nums[right];
        }

        while(left<=right){
            int mid = left + (right-left)/2;

            if(mid>0 && mid <n-1 && (nums[mid-1] != nums[mid] && nums[mid] != nums[mid+1])){
                return nums[mid];
            }

            // Intuition is if nums[mid] is at even index means it is the start sequence
            // if it is start sequence then mid+1 element should also be nums[mid]
            // if nums[mid] is in odd sequence then nums[mid-1] should be start sequence and both should be same
            // if this condition is satisfied then our non duplicate is not in left to mid range we have to search from mid + 1
            // similarly if this condition fails then it is in left to mid-1 range

            if(
                (mid %2 == 0 && nums[mid] == nums[mid+1]) 
                    ||
                (mid %2 == 1 && nums[mid] == nums[mid-1])
            ){ // move to right
                left = mid + 1;
            }else{
                right = mid - 1;
            }

        }

        return -1;
        
    }
}
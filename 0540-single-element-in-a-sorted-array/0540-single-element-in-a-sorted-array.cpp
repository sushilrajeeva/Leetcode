class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {

        int n = nums.size();
        int left = 0;
        int right = n-1;

        // checking for edge cases
        if (n==1){
            return nums[0];
        }else if (nums[0] != nums[1]){
            return nums[0];
        }else if (nums[right] != nums[right-1]){
            return nums[right];
        }

        while (left<=right){
            int mid = left + (right-left)/2;

            // check if mid is the non duplicate
            if(mid > 0 && mid < n-1 && nums[mid-1] != nums[mid] && nums[mid] != nums[mid+1]){
                return nums[mid];
            }

            // check if the mid is the start sequence or the end sequence
            // if it is start sequence then mid + 1 should also be same as nums[mid] (starts with even index)
            // if it is end sequene then mid -1 should be same as nums[mid] (ends with odd index)
            // if this is true then our non duplicate is not present in left to mid range we have to move to mid + 1
            // if false then we should see it in left to mid-1 range
            if (
                (mid %2 == 0 && nums[mid] == nums[mid+1]) || (mid %2 == 1 && nums[mid] == nums[mid-1])
            )
                {
                    // not present in left to mid range, move left to mid + 1
                
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            
        }

        return -1;
        
    }
};
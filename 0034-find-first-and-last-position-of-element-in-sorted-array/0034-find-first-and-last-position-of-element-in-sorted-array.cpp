class Solution {
public:

    int lowerBound(vector<int>& nums, int target){

        int n = nums.size();
        int left = 0;
        int right = n-1;

        while(left<=right){
            int mid = left + (right-left)/2;

            if(nums[mid]>=target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }

        if(left >= n || nums[left] != target){
            return -1;
        }
        
        return left;

    }

    int upperBound(vector<int>& nums, int target){

        int n = nums.size();
        int left = 0;
        int right = n-1;

        while(left<=right){
            int mid = left + (right-left)/2;

            if(nums[mid]<=target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        if(nums[right] != target){
            return -1;
        }
        
        return right;

    }

    vector<int> searchRange(vector<int>& nums, int target) {
        

        int leftIndex = lowerBound(nums, target);
        if(leftIndex == -1){
            return vector<int> {-1, -1};
        }
        int rightIndex = upperBound(nums, target);

        return vector<int>{leftIndex, rightIndex};

    }
};
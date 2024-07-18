class Solution {

    public int lowerBound(int[] nums, int target){
        int n = nums.length;
        int left = 0;
        int right = n-1;

        while(left<=right){
            int mid = left + (right - left)/2;

            if(nums[mid]>=target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }

        if (left>=n || nums[left] != target){
            return -1;
        }
        return left;
    }

    public int upperBound(int[] nums, int target){
        int n = nums.length;
        int left = 0;
        int right = n-1;

        while(left<=right){
            int mid = left + (right - left)/2;

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

    public int[] searchRange(int[] nums, int target) {
        
        int leftIndex = lowerBound(nums, target);
        if(leftIndex == -1){
            return new int[]{-1, -1};
        }
        int rightIndex = upperBound(nums, target);
        return new int[]{leftIndex, rightIndex};

    }
}
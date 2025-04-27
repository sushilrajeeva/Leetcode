class Solution {
    public int search(int[] nums, int target) {
        // checking if array is shifted or not
        int n = nums.length;
        if (n == 1) {
            return nums[0] == target ? 0 : -1;
        }


        if (n == 2) {
            int res = -1;
            if (nums[0] == target) {
                res = 0;
            } else if (nums[1] == target) {
                res = 1;
            }
            return res;
        }

        if (nums[0] < nums[n-1]) {
            return binarySearch(nums, 0, n-1, target);
        }

        int left = 0;
        int right = n - 1;

        while (left <= right) {
            // I have to check where the shift happens
            int mid = (int)(left + (right - left)/2);

            if (mid > 0 && mid < n - 1 && nums[mid - 1] <= nums[mid] && nums[mid+1] < nums[mid]){
                int op1 = binarySearch(nums, 0, mid, target);
                int op2 = binarySearch(nums, mid+1, n-1, target);

                return op1 != -1 ? op1 : op2;
            }

            if (mid < n-1 && nums[mid] > nums[n-1]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    public int binarySearch(int[] nums, int left, int right, int target) {
        
        while (left <= right) {
            int mid = (int) (left + (right - left) / 2);

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}
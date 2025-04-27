class Solution {
    public int search(int[] nums, int target) {
        // checking if array is shifted or not
        int n = nums.length;
        if (n == 0) return -1;
        if (n == 1) {
            return nums[0] == target ? 0 : -1;
        }

        if (isRotated(nums)){
            int breakIndex = getBreakIndex(nums);
            if (nums[breakIndex] == target) { 
                return breakIndex;
            }
            int firstPart = binarySearch(nums, 0, breakIndex, target);
            if (firstPart == -1) {
                return binarySearch(nums, breakIndex, n-1, target);
            }
            return firstPart;
        }

        return binarySearch(nums, 0, n-1, target);


    }

    public boolean isRotated(int[] nums) {
        return nums[0] > nums[nums.length-1];
    }

    public int getBreakIndex(int[] nums) {
        int left = 0;
        int n = nums.length;
        int right = n - 1;

        while (left <= right) {
            int mid = (int)(left + (right - left) / 2);

            if (mid > 0 && mid < n - 1 && nums[mid - 1] > nums[mid] && nums[mid] < nums[mid + 1]) {
                return mid;
            }

            if (nums[mid] > nums[n-1]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }

    public int binarySearch(int[] nums, int left, int right, int target) {
        
        while (left <= right) {
            int mid = (int) (left + (right - left) / 2);

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }
}
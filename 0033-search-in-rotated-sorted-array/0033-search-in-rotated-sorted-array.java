class Solution {
    public int search(int[] nums, int target) {

        int n = nums.length;

        if (n == 0){
            return -1;
        }
        if (nums[0] == target) {
            return 0;
        }
        if (nums[n - 1] == target) {
            return n - 1;
        }

        if (isRotated(nums)) {
            // do something
            int breakingIndex = getBreakingIndex(nums);
            int firstPart = binarySearch(nums, 0, breakingIndex - 1, target);
            if ((firstPart != -1) && (nums[firstPart] == target)) {
                return firstPart;
            }
            return binarySearch(nums, breakingIndex, n - 1, target);
        }
        return binarySearch(nums, 0, n-1, target);
        
    }

    private int getBreakingIndex(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;

        while (left <= right) {
            int mid = (int)(left + (right - left)/2);

            if (isValidIndex(mid, n) && isBreakingPoint(nums, mid)) {
                return mid;
            }

            if (nums[mid] >= nums[n - 1]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }

    private boolean isValidIndex(int mid, int n) {
        return (mid > 0 && mid < n - 1);
    }

    private boolean isBreakingPoint(int[] nums, int mid) {
        return (nums[mid] < nums[mid - 1] && nums[mid] < nums[mid + 1]);
    }

    private boolean isRotated(int[] nums) {
        return nums[0] > nums[nums.length - 1];
    }

    private int binarySearch(int[] nums, int left, int right, int target) {
        while (left <= right) {
            int mid = (int)(left + (right - left)/2);

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
class Solution {
    public int findMin(int[] nums) {

        int n = nums.length;
        if (n == 1) return nums[0];

        if (nums[0] < nums[n-1]) return nums[0];

        int left = 0;
        int right = n - 1;

        while (left <= right) {
            int mid = (int) (left + (right - left) / 2);

            if (mid < n - 1 && nums[mid] > nums[mid+1]) return nums[mid + 1];

            if (mid > 0 && nums[mid - 1] > nums[mid]) return nums[mid];

            if (nums[mid] > nums[n-1]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
        
    }
}
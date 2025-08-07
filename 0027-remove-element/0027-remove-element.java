class Solution {
    public int removeElement(int[] nums, int val) {

        int slow = 0;
        int fast = 0;

        while (fast < nums.length) {
            if (nums[fast] != val) {
                int temp = nums[slow];
                nums[slow] = nums[fast];
                slow += 1;
            }
            fast += 1;
        }
        return slow;
    }
}
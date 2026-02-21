class Solution {
    public int countKDifference(int[] nums, int k) {
        int count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int target1 = k+nums[i];
            int target2 = nums[i] - k;

            if (map.containsKey(target1)) {
                count += map.get(target1);
            }

            if (map.containsKey(target2)) {
                count += map.get(target2);
            }
            
            int value = 0;
            if (map.containsKey(nums[i])) {
                value = map.get(nums[i]);
            }
            map.put(nums[i], value + 1);
        }
        return count;
    }
}
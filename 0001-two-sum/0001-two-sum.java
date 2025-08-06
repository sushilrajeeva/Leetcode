class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>();
        int[] result = {-1, -1};

        for(int i=0; i<nums.length; i++) {
            int key = target-nums[i];
            if (seen.containsKey(key)) {
                result[0] = seen.get(key);
                result[1] = i;
                return result;
            }
            seen.put(nums[i], i);
        }

        return result;
        
    }
}
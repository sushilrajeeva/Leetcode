class Solution {
    public int subarraySum(int[] nums, int k) {

        int count = 0;
        int currentSum = 0;

        HashMap<Integer, Integer> prefixSumCount = new HashMap<>();
        prefixSumCount.put(0, 1);

        for (int num : nums) {
            currentSum += num;
            int target = currentSum - k;
            if (prefixSumCount.containsKey(target)) {
                count += prefixSumCount.get(target);
            }
            int value = 1;
            if (prefixSumCount.containsKey(currentSum)) {
                value += prefixSumCount.get(currentSum);
            }
            prefixSumCount.put(currentSum, value);
        }

        return count;
        
    }
}
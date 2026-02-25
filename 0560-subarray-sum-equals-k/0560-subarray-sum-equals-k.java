class Solution {
    public int subarraySum(int[] nums, int k) {

        int count = 0;
        int currentSum = 0;

        HashMap<Integer, Integer> sumDict = new HashMap<>();
        sumDict.put(0, 1);

        for (Integer num: nums) {
            currentSum += num;

            if (sumDict.containsKey(currentSum - k)) {
                count += sumDict.get(currentSum - k);
            }

            sumDict.put(currentSum, sumDict.getOrDefault(currentSum, 0) + 1);
        }

        return count;
        
    }
}

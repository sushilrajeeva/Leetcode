class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        int n1 = nums1.length;
        int n2 = nums2.length;

        Map<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n2; i++){
            hashMap.put(nums2[i], i);
        }

        Stack<Integer> stack = new Stack<>();

        for (int i = n2-1; i >= 0; i--) {
            if (stack.isEmpty()) {
                stack.push(nums2[i]);
                nums2[i] = -1;
            } else {
                while (!stack.isEmpty() && stack.peek() <= nums2[i]){
                    stack.pop();
                }
                if (stack.isEmpty()) {
                    stack.push(nums2[i]);
                    nums2[i] = -1;
                } else {
                    int ele = nums2[i];
                    nums2[i] = stack.peek();
                    stack.push(ele);
                }
            }
        }

        for (int i = 0; i < n1; i++) {
            int ele = nums1[i];
            nums1[i] = nums2[hashMap.get(ele)];
        }

        return nums1;
        
    }
}
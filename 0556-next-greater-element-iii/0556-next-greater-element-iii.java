class Solution {
    public int nextGreaterElement(int n) {

        char[] digits = String.valueOf(n).toCharArray();
        int m = digits.length;
        int i = m - 2;
        while (i >= 0 && digits[i] >= digits[i+1]) {
            i -= 1;
        }

        if (i < 0) return -1;
        int j = m - 1;

        while (digits[j] <= digits[i]) {
            j -= 1;
        }

        char temp = digits[i];
        digits[i] = digits[j];
        digits[j] = temp;

        int left = i + 1;
        int right = m - 1;
        while (left < right) {
            char t = digits[left];
            digits[left] = digits[right];
            digits[right] = t;
            left += 1;
            right -= 1;
        }

        long result = Long.parseLong(new String(digits));
        return (result <= Integer.MAX_VALUE) ? (int) result : -1;


        
    }
}
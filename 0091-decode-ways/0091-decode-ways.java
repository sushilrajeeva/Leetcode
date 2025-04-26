class Solution {
    public int numDecodings(String s) {

        // get length of the string
        int n = s.length();

        if (n == 0) return 0;

        int prev_1 = (s.charAt(0) == '0') ? 0 : 1;
        int prev_2 = 1;

        if (prev_1 == 0) return 0;

        for (int i = 2; i <= n; i++) {
            char cur = s.charAt(i-1);
            int computation = 0;
            if (cur != '0'){
                computation += prev_1;
            }  
            
            char prev = s.charAt(i-2);

            int twoDigit = (prev - '0') * 10 + (cur - '0');

            if (twoDigit >= 10 && twoDigit <= 26) {
                computation += prev_2;
            }  

            prev_2 = prev_1;
            prev_1 = computation;

        }
        return prev_1;
        
    }
}
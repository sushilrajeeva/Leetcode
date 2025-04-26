class Solution {
    public int numDecodings(String s) {

        // get length of the string
        int n = s.length();

        if (n == 0) return 0;

        int [] dp = new int[n+1];

        dp[0] = 1;
        dp[1] = (s.charAt(0) == '0') ? 0 : 1;
        if (dp[1] == 0) return 0;

        for (int i = 2; i <= n; i++) {
            char cur = s.charAt(i-1);
            if (cur != '0'){
                dp[i] += dp[i-1];
            }  
            
            char prev = s.charAt(i-2);

            int twoDigit = (prev - '0') * 10 + (cur - '0');

            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i-2];
            }  
        }
        return dp[n];
        
    }
}
class Solution {
    public boolean checkOnesSegment(String s) {

        boolean flag = false;
        int count = 0;
        int n = s.length();
        for (int i = 0; i<n; i++) {
            if (flag) {
                if (s.charAt(i) != '1') {
                    flag = false; 
                }
            } else {
                if (s.charAt(i) == '1') {
                    flag = true;
                    count += 1;
                }
            }
        }

        return (count == 1);
        
    }
}
class Solution {
    public int lengthOfLongestSubstring(String s) {

        int left = 0;
        int right = 0;
        int maxLen = 0;

        int[] seen = new int[128];

        int n = s.length();

        while (right < n) {
            char end = s.charAt(right);
            if (seen[(int)end] == 0) {
                seen[(int)end] = 1;
                right += 1;
            } else {
                char start = s.charAt(left);
                seen[(int)start] = 0;
                left += 1;
            }

            maxLen = Math.max(maxLen, right - left);
        }

        return maxLen;
        
    }
}

// class Solution:
//     def lengthOfLongestSubstring(self, s: str) -> int:
        
//         left: int = 0
//         right: int = 0
//         maxLen: int = 0
            
//         seen = [0] * 128
        
//         n: int = len(s)
            
//         while right < n:
//             ele = s[right]
//             if seen[ord(ele)] == 0:
//                 seen[ord(ele)] = 1
//                 right += 1
//             else:
//                 seen[ord(s[left])] = 0
//                 left += 1
//             maxLen = max(maxLen, right - left)
            
//         return maxLen
        
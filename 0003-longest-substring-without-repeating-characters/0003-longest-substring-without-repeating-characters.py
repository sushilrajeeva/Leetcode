class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left: int = 0
        right: int = 0
        maxLen: int = 0
            
        seen = [0] * 128
        
        n: int = len(s)
            
        while right < n:
            ele = s[right]
            if seen[ord(ele)] == 0:
                seen[ord(ele)] = 1
                right += 1
            else:
                seen[ord(s[left])] = 0
                left += 1
            maxLen = max(maxLen, right - left)
            
        return maxLen
        
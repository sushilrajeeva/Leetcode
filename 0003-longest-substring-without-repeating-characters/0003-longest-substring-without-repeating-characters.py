class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left: int = 0
        right: int = 0
        maxLen: int = 0
            
        seen = set()
        
        n: int = len(s)
            
        while right < n:
            ele = s[right]
            if ele not in seen:
                seen.add(ele)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            maxLen = max(maxLen, right - left)
            
        return maxLen
        
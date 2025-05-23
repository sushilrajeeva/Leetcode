class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        seen: set = set()

        left: int = 0
        right: int = 0
        maxLen: int = 0

        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            maxLen = max(maxLen, right - left)

        return maxLen


        
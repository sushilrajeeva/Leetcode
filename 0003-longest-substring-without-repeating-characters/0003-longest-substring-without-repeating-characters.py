class Solution:

    def getCharPos(self, s: str) -> int:
        return ord(s) - 97

    def lengthOfLongestSubstring(self, s: str) -> int:

        l: int = 0
        r: int = 0
        maxLen: int = 0

        seen: set() = set()

        left: int = 0
        n: int = len(s)

        right: int = 0

        while right < n:
            if not s[right] in seen:
                seen.add(s[right])
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            maxLen = max(maxLen, right - left)

        return maxLen
                
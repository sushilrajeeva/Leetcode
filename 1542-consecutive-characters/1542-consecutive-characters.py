class Solution:
    def maxPower(self, s: str) -> int:
        if not s: return 0
        maxLen = 1
        curLen = 1
        ele = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curLen += 1
                maxLen = max(maxLen, curLen)
            else:
                maxLen = max(maxLen, curLen)
                curLen = 1
        maxLen = max(maxLen, curLen)
        return maxLen
                

        
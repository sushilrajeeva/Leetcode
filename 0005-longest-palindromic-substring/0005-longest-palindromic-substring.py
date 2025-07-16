class Solution:
    def longestPalindrome(self, s: str) -> str:
        s2 = s[::-1]
        n = len(s)

        left, right = 0, n-1
        maxLen = 0

        while left < right:
            if s[left] != s2[left]:
                left += 1
            elif s[right] != s2[right]:
                right -= 1
            else:
                return s[left : right + 1]

        return ""


        
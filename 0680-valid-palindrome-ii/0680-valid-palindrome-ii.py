class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        left = 0
        n = len(s)
        right = n - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            count += 1
            if count > 1: return False
            if s[left] == s[right - 1]:
                right -= 1
            else: left += 1
        return True
        
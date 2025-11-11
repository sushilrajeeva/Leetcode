class Solution:
    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else: return False
        return True

    def validPalindrome(self, s: str) -> bool:
        count = 0
        left = 0
        n = len(s)
        right = n - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left, right-1) or self.isPalindrome(s, left+1, right)
            left += 1
            right -= 1
        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left: int = 0
        n: int = len(s)
        right: int = n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): return False

            left +=1
            right -= 1

        return True
        
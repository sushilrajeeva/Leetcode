class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        reverse_str = s[::-1]

        for i in range(n):
            if s[:n-i] == reverse_str[i:]:
                return reverse_str[:i] + s
        return ""
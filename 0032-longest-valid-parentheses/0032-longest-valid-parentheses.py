class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left: int = 0
        right: int = 0
        maxi: int = 0

        for ch in s:
            if ch == '(':
                left += 1
            else: right += 1

            if left == right:
                maxi = max(maxi, left * 2)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0

        for i in reversed(range(len(s))):
            ch = s[i]
            if ch == '(':
                left += 1
            else: right += 1

            if left == right:
                maxi = max(maxi, left * 2)
            elif left > right:
                left = 0
                right = 0

        return maxi
        
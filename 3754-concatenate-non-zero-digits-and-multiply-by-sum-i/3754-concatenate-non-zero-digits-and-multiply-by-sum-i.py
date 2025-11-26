class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        x = 0
        while n > 0:
            digit = n % 10
            total += digit
            x = x if digit == 0 else x * 10 + digit
            n = n // 10

        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        return total * rev
        
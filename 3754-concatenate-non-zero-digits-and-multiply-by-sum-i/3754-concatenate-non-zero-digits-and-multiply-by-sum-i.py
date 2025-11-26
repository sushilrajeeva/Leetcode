class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        x = 0
        place = 1
        while n > 0:
            digit = n % 10
            total += digit
            
            if digit != 0:
                x = digit * place + x
                place = place * 10
            
            n = n // 10
            

        return total * x
        
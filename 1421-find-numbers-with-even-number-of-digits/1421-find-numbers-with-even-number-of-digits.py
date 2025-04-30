class Solution:
    def has_even_digits(self, num: int) -> bool:
        digit_count = 0
        while num:
            digit_count += 1
            num //= 10
        return digit_count % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        evenDigits: int = 0

        for num in nums:
            if self.has_even_digits(num): evenDigits += 1
        
        return evenDigits
        
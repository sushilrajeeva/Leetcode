class Solution:
    def find_digits(self, num: int) -> int:
        return len(str(num))

    def findNumbers(self, nums: List[int]) -> int:
        evenDigits: int = 0
        n: int = len(nums)

        for num in nums:
            if self.find_digits(num)%2 == 0: evenDigits += 1
        
        return evenDigits
        
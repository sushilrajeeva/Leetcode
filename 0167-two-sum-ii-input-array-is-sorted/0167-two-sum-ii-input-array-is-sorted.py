class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n: int = len(numbers)
        left: int = 0
        right: int = n - 1

        while left < right:
            total: int = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
        
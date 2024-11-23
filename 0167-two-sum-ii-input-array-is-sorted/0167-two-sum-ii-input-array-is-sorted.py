class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # There is a guaranteed solution
        # there are always valid inputs

        # Edge case 1: I find my solution in first two , last two or first and last position , avoiding unnecessary computaiton 

        pairs = [[0, 1], [-1, -2]]
        n = len(numbers)

        for pair in pairs:
            if numbers[pair[0]] + numbers[pair[1]] == target:
                first = pair[0] + 1 if pair[0] >= 0 else len(numbers) + pair[0] + 1
                second = pair[1] + 1 if pair[1] >= 1 else len(numbers) + pair[1] + 1
                return [min(first, second), max(first, second)]

        left = 0
        right = n - 1

        while left < right:
            if numbers[left] + numbers[right] == target: return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: left +=1

        return [left + 1, right + 1]
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n: int = len(numbers)

        # checking first and last
        if numbers[0] + numbers[1] == target: return [1, 2]
        if numbers[-1] + numbers[-2] == target: return [n-1, n]

        left: int = 0
        right: int = n-1

        while left < right:
            cal: int = numbers[left] + numbers[right]
            if cal == target: return [left+1, right+1]
            if cal < target:
                left +=1
            else: right -= 1

        return [-1, -1]

            


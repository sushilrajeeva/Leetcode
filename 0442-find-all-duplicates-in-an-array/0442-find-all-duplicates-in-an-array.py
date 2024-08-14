class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res: List[int] = []
        n: int = len(nums)

        if n == 1: return res

        # convert all nums[i] to negative, if it is already neg then add to res

        for i in range(n):
            key: int = abs(nums[i]) - 1
            if nums[key] < 1: res.append(key+1)
            else: nums[key] *= -1

        return res
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n: int = len(nums)
        nums.sort()
        
        for i in range(n-2):
            a: int = nums[i]
            if i > 0 and nums[i-1] == a:
                continue
            left: int = i + 1
            right: int = n - 1

            while left < right:
                total = a + nums[left] + nums[right]
                if total == 0:
                    res.append([a, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
        
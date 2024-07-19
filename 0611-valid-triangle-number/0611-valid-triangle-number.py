class Solution:
    
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n-1, 1, -1):
            # let c b the highest
            c = nums[i]
            left = 0
            right = i - 1
            while left<right:
                a = nums[left]
                b = nums[right]
                if a+b>c:
                    count += right-left
                    right -= 1
                else:
                    left += 1

        return count
                    
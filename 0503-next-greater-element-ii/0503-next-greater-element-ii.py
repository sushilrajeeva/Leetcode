class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        stack = []
        n = len(nums)
        res = [0] * n
        for i in reversed(range(2*n)):

            while (stack and stack[-1] <= nums[i%n]):
                stack.pop()
            
            if i < n:
                res[i] = -1 if not stack else stack[-1]
            
            stack.append(nums[i%n])

        return res
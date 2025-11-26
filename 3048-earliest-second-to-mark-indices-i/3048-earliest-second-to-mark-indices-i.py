class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        left, right = 0, len(changeIndices)+1
        while left < right:
            mid = left + (right-left)//2
            if self.isOK(mid, nums, changeIndices):
                right = mid
            else:
                left = mid+1
        if left == len(changeIndices)+1: return -1
        return left
            
            
    def isOK(self, steps, nums, changeIndices):
        n = len(nums)
        visited = set()
        ops = 0
        for i in range(steps-1, -1, -1):
            j = changeIndices[i]
            if j not in visited:
                ops += nums[j-1]
                visited.add(j)
            elif ops:
                ops -= 1
        if len(visited) < n: return False
        return ops == 0
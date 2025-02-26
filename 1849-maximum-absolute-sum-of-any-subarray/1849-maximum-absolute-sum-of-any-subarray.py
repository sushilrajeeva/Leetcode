class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        maxPos: int = float("-inf")
        minNeg: int = float("inf")
        curPosSum: int = 0
        curNegSum: int = 0
        for num in nums:
            curPosSum += num
            curNegSum += num
            maxPos = max(maxPos, curPosSum)
            minNeg = min(minNeg, curNegSum)
            if curPosSum < 0:
                curPosSum = 0
            if curNegSum > 0:
                curNegSum = 0

        return max(abs(maxPos), abs(minNeg))
            
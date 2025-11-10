class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeq = -1

        for num in nums:
            if num - 1 not in numSet:
                curSeq = 1
                while num + curSeq in numSet:
                    curSeq += 1
                maxSeq = max(maxSeq, curSeq)
        return maxSeq

        
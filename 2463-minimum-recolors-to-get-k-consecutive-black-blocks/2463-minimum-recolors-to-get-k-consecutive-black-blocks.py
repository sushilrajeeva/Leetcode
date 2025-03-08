class Solution:

    def getBlackCount(self, blocks: str, k: int) -> int:
        count: int = 0
        for i in range(k):
            if blocks[i] == 'B': count += 1
        return count

    def minimumRecolors(self, blocks: str, k: int) -> int:
        n: int = len(blocks)
        blacks: int = -1
        minOperations: int = float("inf")

        for i in range(n-k+1): #O(n-k+1)
            if i == 0:
                blacks = self.getBlackCount(blocks, k) #O(k)
            else:
                if blocks[i-1] == 'B':
                    blacks -= 1
                if blocks[i+k-1] == 'B':
                    blacks += 1
            operations = k - blacks
            if operations < minOperations:
                minOperations = operations

        return minOperations


from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n: int = len(cardPoints)

        # If all cards are to be picked
        if n == k:
            return sum(cardPoints)

        # If only one card is to be picked
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])

        left: int = 0
        right: int = n - k
        
        rightTotal: int = sum(cardPoints[right:])

        maxSum: int = rightTotal

        while right < n:
            rightTotal += (cardPoints[left] - cardPoints[right])
            maxSum = max(maxSum, rightTotal)
            right += 1
            left += 1

        return maxSum
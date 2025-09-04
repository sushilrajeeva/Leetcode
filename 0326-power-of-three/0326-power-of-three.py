class Solution:

    def binarySearch(self, n: int) -> bool:
        left = 0
        right = 31

        while left <= right:
            mid = int(right - (right - left)/2)
            compute = pow(3, mid)
            if compute == n:
                return True
            if compute < n:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        if n % 2 == 0: return False

        return self.binarySearch(n)
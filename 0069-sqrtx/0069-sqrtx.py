class Solution:
    def mySqrt(self, x: int) -> int:

        # we know that sqrt of x is in range of 0 to x/2+1

        left, right = 0, 1 + (x//2)

        while left<=right:

            mid = left + (right-left)//2

            square = mid*mid

            if square==x:
                return mid

            if square<x:
                left = mid + 1
            else:
                right = mid - 1

        return right
        
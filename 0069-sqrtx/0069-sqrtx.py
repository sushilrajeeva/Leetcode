class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left < right:
            mid = (right + left)//2
            compute = mid * mid
            if compute == x:
                return mid
            if compute < x:
                left = mid + 1
            else:
                right = mid - 1

        return right if right * right <= x else right - 1



        
class Solution:

    # given the number that represents a row, return overal how many coins will be there
    def getCoins(self, num) -> int:
        if num%2 == 0:
            return (num//2) * (num+1)
        return num*((num+1)//2)

    def arrangeCoins(self, n: int) -> int:

        left = 0
        right = n

        while left<=right:
            mid = left + (right-left)//2
            coins = self.getCoins(mid)
            if coins == n:
                return mid
            
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1

        return right
        
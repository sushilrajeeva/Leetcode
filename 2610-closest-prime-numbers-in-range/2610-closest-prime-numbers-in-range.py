import heapq
class Solution:

    def getPrimes(self, left: int, right: int) -> List[int]:
        buffer: List[int] = [True] * (right + 1)

        buffer[0] = False
        buffer[1] = False
        
        for i in range(2, int(sqrt(right)) + 1):
            if buffer[i]:
                for j in range(i+i, right + 1, i):
                    buffer[j] = False

        return [i for i in range(left, right + 1) if buffer[i]]

    def closestPrimes(self, left: int, right: int) -> List[int]:

        if left == right: return [-1, -1]
        primes = self.getPrimes(left, right)

        if len(primes) < 2: return [-1, -1]
        print(primes)

        num1: int = primes[0]
        num2: int = primes[1]
        minDiff: int = abs(num1 - num2)
        
        for i in range(1, len(primes)):
            diff = abs(primes[i] - primes[i-1])

            if diff < minDiff:
                minDiff = diff
                num1 = primes[i-1]
                num2 = primes[i]


        return [num1, num2]
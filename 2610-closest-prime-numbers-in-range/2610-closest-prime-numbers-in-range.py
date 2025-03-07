class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Create a sieve for all numbers up to right
        sieve = [True] * (right + 1)
        sieve[0:2] = [False, False]  # 0 and 1 are not primes
        
        # Mark non-prime numbers using the Sieve of Eratosthenes
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
                    
        # Collect primes in the given range [left, right]
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        # If there are fewer than two primes, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]
        
        # Find the closest pair of primes
        closest_pair = [primes[0], primes[1]]
        min_diff = primes[1] - primes[0]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i - 1], primes[i]]
                
        return closest_pair

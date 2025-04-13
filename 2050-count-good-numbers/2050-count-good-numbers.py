class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # Fast modular exponentiation: (base^exp) % MOD
        def mod_pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result

        # Count of digits at even positions (0,2,4,...): use 5 options
        even_positions = (n + 1) // 2
        # Count of digits at odd positions (1,3,5,...): use 4 options
        odd_positions = n // 2

        return (mod_pow(5, even_positions) * mod_pow(4, odd_positions)) % MOD

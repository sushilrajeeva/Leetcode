class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def algo(x: int) -> bool:
            if x == 1: return True
            if x in seen: return False
            seen.add(x)
            total = 0
            while x != 0:
                total += (x % 10) ** 2
                x = x//10
            return algo(total)

        return algo(n)
        
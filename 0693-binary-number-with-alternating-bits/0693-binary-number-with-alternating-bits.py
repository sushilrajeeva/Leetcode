class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        rep = bin(n)[2:]

        n = len(rep)
        if n <= 1: return True

        for i in range(1, n):
            if rep[i-1] == rep[i]: return False
        
        return True

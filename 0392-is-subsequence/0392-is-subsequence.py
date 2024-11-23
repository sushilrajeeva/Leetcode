class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t): return False
        if len(s) == 0: return True

        limit: int = len(s)
        j: int = 0

        for i in range(len(t)):
            if s[j] == t[i]: j += 1
            if j == limit: return True

        return False
        
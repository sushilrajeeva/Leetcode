class Solution:

    def getIndex(self, ch: str) -> int:
        return ord(ch) - 97

    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n: return False

        s_arr = [0] * 26
        t_arr = [0] * 26

        for i in range(m):
            s_arr[self.getIndex(s[i])] += 1
            t_arr[self.getIndex(t[i])] += 1

        for i in range(26):
            if s_arr[i] != t_arr[i]: return False

        return True
        
class Solution:

    def getIndex(self, ch: str) -> int:
        return ord(ch) - 97

    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n: return False

        freq = [0] * 26

        for i in range(m):
            freq[self.getIndex(s[i])] += 1
            freq[self.getIndex(t[i])] -= 1

        for i in range(26):
            if freq[i] != 0: return False

        return True
        
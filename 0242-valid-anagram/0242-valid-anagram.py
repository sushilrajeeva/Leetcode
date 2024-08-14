class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n: int = len(s)
        m: int = len(t)

        if n != m: return False

        alphabetBuffer: List[int] = [0] * 26

        for i in range(n):
            alphabetBuffer[ord(s[i])-97] += 1
            alphabetBuffer[ord(t[i])-97] -= 1

        for i in range(26):
            if alphabetBuffer[i] != 0: return False
        
        return True
        
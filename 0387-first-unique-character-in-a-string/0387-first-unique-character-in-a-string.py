class Solution:
    def firstUniqChar(self, s: str) -> int:

        n: int = len(s)
        if n == 1: return 0
        buffer: List[int] = [0]*26
        hasDuplicate: bool = False

        for i in range(n):
            key: int = ord(s[i]) - 97
            buffer[key] += 1
            if buffer[key] > 1: hasDuplicate = True
        
        if not hasDuplicate: return 0

        for i in range(n):
            key: int = ord(s[i]) - 97
            if buffer[key] == 1: return i
        return -1



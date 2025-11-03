class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = len(ransomNote)
        m = len(magazine)

        if n > m: return False

        charMap = [0] * 26

        for ch in magazine:
            charMap[ord(ch) - 97] += 1
        
        for ch in ransomNote:
            charMap[ord(ch) - 97] -= 1
            if charMap[ord(ch) - 97] < 0:
                return False

        return True

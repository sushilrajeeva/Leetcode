class Solution:

    def getCharVal(self, charecter: str) -> int:
        return ord(charecter) - 97

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine): return False
        
        temp = [0] * 26

        for ele in magazine:
            temp[self.getCharVal(ele)] += 1

        for ele in ransomNote:
            temp[self.getCharVal(ele)] -= 1
            if temp[self.getCharVal(ele)] < 0:
                return False
        return True




        
class Solution:

    def getCharVal(self, ele: str) -> int:
        return ord(ele) - 97

    def firstUniqChar(self, s: str) -> int:
        temp = [0] * 26

        for ele in s:
            temp[self.getCharVal(ele)] += 1
        
        
        for index in range(len(s)):
            if temp[self.getCharVal(s[index])] == 1: return index

        return -1

        
class Solution:
    def computeIndex(self, x: str) -> int:
        return ord(x) - ord('a')
    def firstUniqChar(self, s: str) -> int:
        temp = [0] * 26

        for ele in s:
            temp[self.computeIndex(ele)] += 1
        
        for index, ele in enumerate(s):
            if temp[self.computeIndex(ele)] == 1:
                return index

        return -1
        
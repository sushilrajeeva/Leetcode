class Solution:
    def computeIndex(self, ele: str) -> int:
        return ord(ele) - ord('a')

    def checkIfPangram(self, sentence: str) -> bool:
        temp = [0] * 26
        for ele in sentence:
            temp[self.computeIndex(ele)] += 1
        
        for count in temp:
            if count == 0:
                return False
        return True
        
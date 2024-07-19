class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:


        for i in range(len(matrix)):
            minimum = min(matrix[i])
            for j in range(len(matrix[0])):
                if matrix[i][j] == minimum:
                    matrix[i][j] *= -1
            print("row", i, ":", matrix[i])
        result = []
        for j in range(len(matrix[0])):
            minMaxEle = 0
            maxEle = float("-inf")

            for i in range(len(matrix)):
                if matrix[i][j] < 0:
                    minMaxEle = max(minMaxEle, abs(matrix[i][j]))
                maxEle = max(maxEle, abs(matrix[i][j]))

            if minMaxEle != 0 and minMaxEle == maxEle:
                result.append(maxEle)
        
        return result
            
        

        
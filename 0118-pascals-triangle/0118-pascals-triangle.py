class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                prev = result[-1]
                prev_ele = prev[0]
                temp = [prev_ele]
                for j in range(1, len(prev)):
                    temp.append(prev_ele + prev[j])
                    prev_ele = prev[j]
                temp.append(1)
                result.append(temp)
        return result


                
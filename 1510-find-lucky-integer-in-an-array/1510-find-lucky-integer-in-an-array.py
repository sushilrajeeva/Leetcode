class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n: int = len(arr)
        temp: List[int] = [0] * (max(arr) + 1)
        res = -1

        for ele in arr:
            temp[ele] += 1

        for i in range(1, max(arr) + 1):
            if i == temp[i]:
                res = max(res, i)
        return res

        
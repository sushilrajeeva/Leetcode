class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def numVal(num: int) -> int:
            res = ""
            num = str(num)

            for ele in num:
                res += str(mapping[int(ele)])
            return int(res)
        my_map = [(key, numVal(key)) for key in nums]

        def sortVal(x):
            return x[1]
        my_map.sort(key=sortVal)

        return [num for num, val in my_map]

        
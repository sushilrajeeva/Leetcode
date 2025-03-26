class Solution:


    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_arr = []
        result = 0

        for row in grid:
            for ele in row:
                nums_arr.append(ele)

        nums_arr.sort()

        n = len(nums_arr)

        median = nums_arr[n//2]
        check: int = median % x

        for num in nums_arr:
            if num % x != check: return -1
            result += abs(median - num) // x
        
        return result

        
    

        

        
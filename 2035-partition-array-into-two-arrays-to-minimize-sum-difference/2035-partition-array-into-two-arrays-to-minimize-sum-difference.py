class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def binarySearch(targetVal, arr):
            low = 0; high = len(arr)-1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == targetVal:
                    return targetVal
                elif arr[mid] < targetVal:
                    low = mid + 1
                else:
                    high = mid - 1
            if high == -1:
                return arr[0]
            elif low == len(arr):
                return arr[-1]
            else:
                if abs(targetVal-arr[low]) < abs(targetVal-arr[high]):
                    return arr[low]
                else:
                    return arr[high]

        def fetchPossibleCombinations(arr):
            """
                Returns a dictionary of numbers
                Key - number of elements in the sum
                Value - Sum value of that particular combination
            """
            def helper(pos, total, count):
                if pos == length:
                    dp[count].add(total)
                else:
                    helper(pos+1, total, count)
                    helper(pos+1, total+arr[pos], count+1)

            length = len(arr); dp = {i: set() for i in range(length+1)}
            helper(0, 0, 0)

            for count, values in dp.items():
                dp[count] = sorted(list(values))
    
            return dp

        length = len(nums); targetLength = length // 2
        totalSum = sum(nums); targetTotal = totalSum // 2
        arr1 = nums[:targetLength]; arr2 = nums[targetLength:]

        dp1 = fetchPossibleCombinations(arr1)
        dp2 = fetchPossibleCombinations(arr2)

        minDiff = float('inf')
        for c1, values1 in dp1.items():
            values2 = dp2[targetLength-c1]

            for val1 in values1:
                val2 = binarySearch(targetTotal-val1, values2)
                minDiff = min(abs(totalSum - 2 * (val1 + val2)), minDiff)

        return minDiff
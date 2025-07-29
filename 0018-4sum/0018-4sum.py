class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Sorting the array in place 
        nums.sort()

        n = len(nums)

        # setting up result array
        result = []

        for i in range(n):

            # condition for i - ensuring ith element is not same as previous ith element
            if i > 0 and nums[i] == nums[i-1]: continue

            for j in range(i+1, n):

                # Condition for j - ensuring jth element is not same as previous jth element
                if j > i+1 and nums[j] == nums[j-1]: continue

                # Setting two pointers
                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # Condition 1 - total < target
                    if total < target:
                        left += 1


                    # Condition 2 - total > target
                    elif total > target:
                        right -= 1


                    # Condition 3 - total = target
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # check if left and right are not same as their previous
                        while left < right and nums[left] == nums[left-1]: left += 1
                        while left < right and nums[right] == nums[right+1]: right -= 1

        return result

        
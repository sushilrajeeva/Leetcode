class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ways = 0
        n = len(nums)
        left = 0
        right = 0
        window_sum = 0

        while right < n:
            # include nums[right] into our window sum
            window_sum += nums[right]

            # if product ≥ k, shrink from the left until it's valid again
            while left <= right and window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1

            # now every subarray ending at `right` with start in [left..right] is valid
            ways += (right - left + 1)

            # move right forward
            right += 1

        return ways

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def binary_search(target, arr):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            idx = binary_search(h, dp)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)
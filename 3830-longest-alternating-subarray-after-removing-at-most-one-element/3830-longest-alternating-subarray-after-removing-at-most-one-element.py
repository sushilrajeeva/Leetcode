class Solution:
    def longestAlternating(self, A: List[int]) -> int:
        n = len(A)

        def cmp(a, b):
            return (a > b) - (a < b)

        l = [1] * n
        for i in range(1, n):
            d = cmp(A[i], A[i - 1])
            if d:
                if i > 1 and cmp(A[i - 1], A[i - 2]) == -d:
                    l[i] = l[i - 1] + 1
                else:
                    l[i] = 2
        r = [1] * n
        for i in range(n - 2, -1, -1):
            d = cmp(A[i + 1], A[i])
            if d:
                if i < n - 2 and cmp(A[i + 2], A[i + 1]) == -d:
                    r[i] = r[i + 1] + 1
                else:
                    r[i] = 2
        res = max(l)
        for i in range(1, n - 1):
            d = cmp(A[i + 1], A[i - 1])
            if d:
                L = l[i - 1] if i > 1 and cmp(A[i - 1], A[i - 2]) == -d else 1
                R = r[i + 1] if i < n - 2 and cmp(A[i + 2], A[i + 1]) == -d else 1
                res = max(res, L + R)
        return res

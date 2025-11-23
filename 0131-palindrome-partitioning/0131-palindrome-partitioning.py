class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def dp(i, curr: list):
            if i == n:
                res.append(curr[:])
                return
            for j in range(i, n):
                curr_substring = s[i:j+1]
                if curr_substring == curr_substring[::-1]:
                    curr.append(curr_substring)
                    dp(j+1, curr)
                    curr.pop()
        dp(0, [])
        return res
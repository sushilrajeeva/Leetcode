class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        temp = []

        def dfs(i):
            if i == len(s):
                res.append(" ".join(temp))
            for w in wordDict:
                n = len(w)
                if (i + n) <= len(s) and s[i: i + n] == w:
                    temp.append(s[i: i + n])
                    dfs(i + n)
                    temp.pop()

        dfs(0)
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n: int = len(s)
        
        res = [""]
        resLen = [0]

        def computePalindrome(l: int, r: int) -> None:
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen[0]:
                    resLen[0] = (r - l + 1)
                    res[0] = s[l: r + 1]
                l -= 1
                r += 1

        for i in range(n):

            # for odd length
            l, r = i, i
            computePalindrome(l, r)
            
            # even length
            l, r = i, i + 1
            computePalindrome(l, r)

        return res[0]

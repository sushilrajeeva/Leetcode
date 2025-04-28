class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n: int = len(s)

        if n > 12: return []

        res: List[int] = []

        def backtrack(i: int, dots: int, currentIP: str) -> None:

            # Exit conditions
            if i == n and dots == 4:
                res.append(currentIP[:-1])
                return
            
            # invalid condition hence exit
            if dots > 4: return

            for j in range(i, min(i+3, n)):
                ele: str = s[i:j+1]
                if int(ele) < 256 and (i == j or ele[0] != '0' ):
                    backtrack(j + 1, dots + 1, currentIP + ele + ".")

        backtrack(0, 0, "")

        return res  
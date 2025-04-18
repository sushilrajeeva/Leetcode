class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1: return "1"

        compute = self.countAndSay(n-1)

        prevEle = None
        count = 0
        
        res = ""

        for i in range(len(compute)):
            if count == 0 or compute[i] != prevEle:
                res += str(count) + prevEle if prevEle else ""
                prevEle = compute[i]
                count = 1
            else:
                count += 1

        if count != 0:
            res += str(count) + prevEle
        
        return res

            
        
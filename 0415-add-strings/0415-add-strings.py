class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        numDict = dict()
        n: int = len(num1)
        m: int = len(num2)

        

        carry = 0
        i: int = n-1
        j: int = m-1
        result = ""

        while i >= 0 or j >= 0 or carry:
            first = ord(num1[i]) - ord('0') if i >= 0 else 0
            second = ord(num2[j]) - ord('0') if j >= 0 else 0 
            res = carry + first + second

            carry = res // 10
            res = res % 10
            result = str(res) + result

            i -= 1
            j -= 1

        return result
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        i = 0

        for ch in s:
            if ch.isdigit():
                num = (num * 10) + int(ch)
            elif ch == "+":
                result += sign * num
                sign = 1
                num = 0
            elif ch == "-":
                result += sign * num
                sign = -1
                num = 0
            elif ch == "(":
                stack.append(result)
                stack.append(sign)

                sign = 1
                result = 0

            elif ch == ")":
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
            
        return result + sign * num

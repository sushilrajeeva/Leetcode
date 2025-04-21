class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        count = 0
        for p in s:
            if p == "(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        count += len(stack)
        return count
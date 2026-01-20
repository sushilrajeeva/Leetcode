class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        memo = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
            }

        for ele in s:
            if not stack or ele in memo:
                stack.append(ele)
            else:
                if memo.get(stack[-1], "-1") != ele:
                    return False
                stack.pop()

        return not stack
        
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapper = {"(": ")",
                    "{": "}",
                    "[": "]"
                }

        for ele in s:
            if not stack and ele in {")", "}", "]"}:
                return False
            elif not stack or ele in {"(", "{", "["}:
                stack.append(ele)
            elif stack and mapper.get(stack[-1]) == ele:
                stack.pop()
            else:
                return False

        if stack:
            return False

        return True

        
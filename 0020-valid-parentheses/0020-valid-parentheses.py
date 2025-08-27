class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        openBrackets = set(mapper.keys())
        closeBrackets = set(mapper.values())

        for ele in s:
            if ele in openBrackets:
                stack.append(ele)
            elif ele in closeBrackets:
                if not stack or mapper[stack[-1]] != ele:
                    return False
                stack.pop()
            else:
                return False

        if stack:
            return False
        return True
            
        
from typing import List
class Solution:
    

    def longestValidParentheses(self, s: str) -> int:
        stack: List[int] = [-1]

        max_len: int = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    cur_len = i - stack[-1]
                    max_len = max(max_len, cur_len)

        return max_len
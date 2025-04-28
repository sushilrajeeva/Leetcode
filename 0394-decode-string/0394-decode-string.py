class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                mini_stack = []
                while stack and stack[-1] != "[":
                    mini_stack.append(stack.pop())
                
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                
                num = 1 if num == "" else int(num[::-1])
                for _ in range(num):
                    for j in reversed(range(len(mini_stack))):
                        stack.append(mini_stack[j])
        return "".join(stack)


        
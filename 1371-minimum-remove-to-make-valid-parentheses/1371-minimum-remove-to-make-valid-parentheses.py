class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        word = []

        for index, value in enumerate(s):
            if value == "(":
                stack.append(index)
                word.append(value)
            elif value == ")" and stack and stack[-1] >=0:
                stack.pop()
                word.append(value)
            elif value != ")":
                word.append(value)
            else:
                word.append(None)

        for i in range(len(stack)):
            index = stack.pop()
            word[index] = None

        output = ""
        for ele in word:
            if ele:
                output += ele
                 
        

        return output
        
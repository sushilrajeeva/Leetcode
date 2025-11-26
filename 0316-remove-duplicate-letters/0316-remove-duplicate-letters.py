class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {ch: i for i, ch in enumerate(s)}

        stack = []
        in_stack = set()

        for i, ch in enumerate(s):
            if ch in in_stack:
                continue

            while stack and stack[-1] > ch and last_index[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(ch)
            in_stack.add(ch)

        return "".join(stack)
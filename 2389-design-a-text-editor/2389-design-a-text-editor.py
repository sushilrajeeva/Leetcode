class TextEditor:

    def __init__(self):
        self.left = []
        self.right = deque([])


    def addText(self, text: str) -> None:
        self.left.extend(text)


    def deleteText(self, k: int) -> int:
        removed = len(self.left[:k])

        while self.left and k:
            self.left.pop()
            k-= 1

        return removed
        
    
    def cursorLeft(self, k: int) -> str:
        while self.left and k:
            self.right.appendleft(self.left.pop())
            k-= 1
            
        return self.getLast10()


    def cursorRight(self, k: int) -> str:
        while self.right and k:
            self.left.append(self.right.popleft())
            k-= 1

        return self.getLast10()


    def getLast10(self) -> str:
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
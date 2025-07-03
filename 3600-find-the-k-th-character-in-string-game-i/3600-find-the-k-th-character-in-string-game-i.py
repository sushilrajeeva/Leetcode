class Solution:

    def magic(self, word: str) -> str:
        res: str = ""
        for ch in word:
            next_ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
            res += next_ch
        return word+res

    def kthCharacter(self, k: int) -> str:
        if k == 1: return "a"

        n: int = 0
        word = "a"

        while n < k:
            word = self.magic(word)
            n = len(word)
        
        return word[k-1]


        
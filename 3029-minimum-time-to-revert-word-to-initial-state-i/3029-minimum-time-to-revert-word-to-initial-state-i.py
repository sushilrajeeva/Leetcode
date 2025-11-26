class Solution:

    def check(self, word: str, target: str) -> bool:
        n: int = len(word)
        for i in range(n):
            if target[i] != '*' and word[i] != target[i]:
                return False
        return True

    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n: int = len(word)
        c: int = 0
        copy: str = word

        while True:
            # perform one operation
            copy = copy[k:] + '*' * k
            c += 1

            if self.check(word, copy):
                return c

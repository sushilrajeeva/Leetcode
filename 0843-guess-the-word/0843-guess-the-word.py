# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: list[str], master: 'Master') -> None:
        def match(guess, target):
            return sum(x == y for x, y in zip(guess, target))
        
        candidates = words[:]
        for _ in range(30):
            best = None
            maxScore = float('inf')
            for word in candidates:
                buckets = [0]*7
                for cand in candidates:
                    buckets[match(word, cand)] += 1
                score = max(buckets)
                if score < maxScore:
                    maxScore = score
                    best = word
            cand = master.guess(best)
            if cand == 6:
                return
            candidates = [word for word in candidates if match(best, word) == cand]
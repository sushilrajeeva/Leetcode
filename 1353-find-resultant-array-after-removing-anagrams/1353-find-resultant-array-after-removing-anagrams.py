from typing import List

class Solution:
    def isAnagram(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq = [0] * 26
        for ch1, ch2 in zip(word1, word2):
            freq[ord(ch1) - ord('a')] += 1
            freq[ord(ch2) - ord('a')] -= 1
        return all(x == 0 for x in freq)

    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if not self.isAnagram(words[i], result[-1]):
                result.append(words[i])
        return result

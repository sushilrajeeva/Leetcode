from collections import Counter
import heapq

class HeapItem:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __lt__(self, to_compare) -> bool:
        if self.count == to_compare.count:
            return self.word > to_compare.word  # reverse lexicographical order for heapq
        return self.count < to_compare.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        wordCount: dict = Counter(words)
        n: int = len(words)
        heap = []
        heapq.heapify(heap)

        for word, count in wordCount.items():
            heapq.heappush(heap, HeapItem(word, count))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            result.append(heapq.heappop(heap).word)
        

        return result[::-1]
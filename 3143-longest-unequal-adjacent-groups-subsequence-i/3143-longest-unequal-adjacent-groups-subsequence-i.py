from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        if n == 0:
            return []
        
        # result list and last-picked group
        res = []
        prev_group = None
        
        # scan through exactly once, picking on every flip
        for i in range(n):
            if prev_group is None or groups[i] != prev_group:
                res.append(words[i])
                prev_group = groups[i]
        
        return res

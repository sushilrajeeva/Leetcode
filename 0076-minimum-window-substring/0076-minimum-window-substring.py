from typing import *
from collections import *
class Solution:

    def isPossible(self, window: Dict[str, int], target: Dict[str, int]) -> bool:
        for ch, count in target.items():
            if window.get(ch, 0) < count: return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        m: int = len(s)
        n: int = len(t)

        if m < n: return ""

        t_map: Dict[str, int] = defaultdict(int)

        for ch in t:
            t_map[ch] += 1

        s_map: Dict[str, int] = defaultdict(int)
        l = 0
        minLen = m
        minRange = [-1, -1]

        for r, ch in enumerate(s):
            s_map[ch] += 1

            while l <= r and self.isPossible(s_map, t_map):
                cur_len = r - l + 1
                if cur_len <= minLen:
                    minLen = cur_len
                    minRange[0] = l
                    minRange[1] = r
                s_map[s[l]] -= 1
                l += 1

        start, end = minRange   
        return s[start: end + 1]

        
        
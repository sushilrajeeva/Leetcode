from collections import defaultdict
from typing import Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        # Build target counts and set up 'formed' tracking
        t_map: Dict[str,int] = defaultdict(int)
        for ch in t:
            t_map[ch] += 1
        required = len(t_map)

        # Window counts and formed counter
        s_map: Dict[str,int] = defaultdict(int)
        formed = 0

        l = 0
        minLen = float('inf')
        minRange = [-1, -1]

        # Expand right pointer r
        for r, ch in enumerate(s):
            s_map[ch] += 1
            # Did we just satisfy one of the target character counts?
            if ch in t_map and s_map[ch] == t_map[ch]:
                formed += 1

            # When all required unique chars are formed, try shrinking
            while l <= r and formed == required:
                cur_len = r - l + 1
                if cur_len < minLen:
                    minLen = cur_len
                    minRange = [l, r]

                # Remove s[l] from window
                left_char = s[l]
                s_map[left_char] -= 1
                l += 1
                # If we fell below the required count, we no longer “form” that char
                if left_char in t_map and s_map[left_char] < t_map[left_char]:
                    formed -= 1
                

        # Return the best window, or "" if none found
        if minRange[0] == -1:
            return ""
        start, end = minRange
        return s[start:end+1]

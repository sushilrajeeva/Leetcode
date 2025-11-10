class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(" ")
        if len(s_arr) != len(pattern):
            return False

        mapp = {}
        seen = set()
        n = len(pattern)
        for i in range(n):
            key = pattern[i]
            value = s_arr[i]
            if key not in mapp:
                if value in seen: return False
                mapp[key] = value
                seen.add(value)
            else:
                if mapp[key] != value: return False

        return True

        
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = defaultdict(int)
        n: int = len(s)
        for char in s:
            char_counts[char] += 1
        max_count = 0
        letter = ''
        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                letter = char

        if max_count > (n + 1)//2:
            return ""

        ans: List[int] = [''] * n
        index = 0

        while char_counts[letter] != 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1
        
        for char, count in char_counts.items():
            while char_counts[char] > 0:
                if index >= n:
                    index = 1
                ans[index] = char
                char_counts[char] -= 1
                index += 2

        return ''.join(ans)
        
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j, length = i, 0
            while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1
            gaps = j - i - 1
            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - length
                even, extra = divmod(spaces, gaps)
                line = ""
                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        line += " " * (even + (1 if extra > 0 else 0))
                        extra -= 1
            res.append(line)
            i = j
        return res
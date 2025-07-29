class Solution:
    def compress(self, chars: List[str]) -> int:
        output: str = ""
        count: int = 1
        cur: str = chars[0]
        output += cur
        n: int = len(chars)
        for i in range(1, n):
            if chars[i] != cur:
                if count != 1:
                    output += str(count)
                output += chars[i]
                count = 1
                cur = chars[i]
            else:
                count += 1
        
        if count > 1:
            output += str(count)
        for index, value in enumerate(output):
            chars[index] = value
        return len(output)

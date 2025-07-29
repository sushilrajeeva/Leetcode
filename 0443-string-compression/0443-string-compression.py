class Solution:
    def compress(self, chars: List[str]) -> int:
        n: int = len(chars)
        seeker: int = 0
        writer: int = 0

        while seeker < n:
            char = chars[seeker]
            count = 0

            while seeker < n and chars[seeker] == char:
                count += 1
                seeker += 1

            chars[writer] = char
            writer += 1

            if count > 1:
                for digit in str(count):
                    chars[writer] = digit
                    writer += 1
            
        return writer
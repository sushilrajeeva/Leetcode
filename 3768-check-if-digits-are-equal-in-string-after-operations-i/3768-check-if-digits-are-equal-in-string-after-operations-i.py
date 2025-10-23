class Solution:
    def hasSameDigits(self, s: str) -> bool:
        count = 0
        while True:
            if len(s) == 2:
                if s[0] != s[1]: return False
                return True
            if len(s) < 2:
                return False

            new_str = ""

            for i in range(len(s) - 1):
                new_str += str((int(s[i]) + int(s[i+1])) % 10)
            
            count += 1
            s = new_str

        return True
        
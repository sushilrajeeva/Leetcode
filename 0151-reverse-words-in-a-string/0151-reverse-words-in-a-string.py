class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        output = ""
        cur = ""

        for i in range(len(s)):
            if s[i] == " ":
                if cur.strip() != "":
                    output = cur + " " + output
                cur = ""
            else:
                cur += s[i]
        output = cur + " " + output
        return output.strip()
        

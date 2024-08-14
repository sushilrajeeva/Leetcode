class Solution:
    
    def reverseVowels(self, s: str) -> str:
        n: int = len(s)
        left: int = 0
        right: int = n - 1
        res: List[str] = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if n == 1: return s

        while left < right:
            while left < right and not (res[left] in vowels): left += 1
            while left < right and not (res[right] in vowels): right -= 1
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return "".join(res)

            

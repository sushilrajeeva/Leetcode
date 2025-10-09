class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n: int = len(skill) # no of wizards
        m: int = len(mana) # no of potions
        f = [0] * (n + 1)

        
        for x in mana:
            for i in range(n):
                f[i + 1] = max(f[i + 1], f[i]) + (skill[i] * x)
            for i in reversed(range(n)):
                f[i] = f[i + 1] - (skill[i] * x)
            
        return f[n]

        
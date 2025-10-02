class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        mapper = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        
        n = len(s)
        res = 0
        index = 0
        while index < n:
            if index + 1 < n and mapper[s[index]] < mapper[s[index + 1]]:
                print(mapper[s[index] + s[index+1]])
                res += mapper[s[index] + s[index+1]]
                index += 2
            else:
                print(mapper[s[index]])
                res += mapper[s[index]]
                index += 1
                
        return res
        
        
        
        
        
class Solution:
        
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num: int = 0
        #123
        for i in range(len(digits)):
            num = (num*10) + digits[i]
            
        num += 1
        
        res: List[int] = []
            
        while num > 0:
            ele = num % 10
            num = num // 10
            
            res.append(ele)
        
        return res[::-1]
        
        
            
        
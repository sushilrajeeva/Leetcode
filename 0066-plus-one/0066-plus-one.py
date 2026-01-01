class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 1
        for i in reversed(range(n)):
            if carry == 1:
                if i == 0:
                    if digits[i] == 9:
                        return [1] + [0] * n
                    
                    digits[i] += 1
                    return digits
                else:
                    if digits[i] == 9:
                        digits[i] = 0
                        carry = 1
                    else:
                        digits[i] += 1
                        carry = 0
            else:
                return digits

        return digits
                
                
        
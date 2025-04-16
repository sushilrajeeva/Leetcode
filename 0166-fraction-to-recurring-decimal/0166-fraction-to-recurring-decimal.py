class Solution:

    def isNeg(self, numerator, denominator) -> bool:
        if numerator < 0 and denominator < 0: return False
        if numerator < 0 or denominator < 0: return True
        return False

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        print("numerator:", numerator, "denominator:", denominator)

        if numerator == 0: return "0"

        sign = "-" if self.isNeg(numerator, denominator) else ""
        n, d = abs(numerator), abs(denominator)

        first_part = n // d
        rem = n % d

        if rem == 0:
            return sign + str(first_part)

        res = [sign + str(first_part), "."]
        seen = {}

        # Long division loop
        while rem:
            # If this remainder was seen, we have a repeating cycle
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, "(")
                res.append(")")
                break
            
            # Record where this remainder first appears
            seen[rem] = len(res)
            
            rem *= 10
            digit = rem // d
            res.append(str(digit))
            rem %= d
        
        return "".join(res)


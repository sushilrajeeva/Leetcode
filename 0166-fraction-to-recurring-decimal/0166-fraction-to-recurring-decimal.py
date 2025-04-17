class Solution:

    def isNegative(self, numerator: int, denominator: int) -> bool:
        if numerator < 0 and denominator < 0: return False
        if numerator < 0 or denominator < 0: return True
        return False

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0: return "0"

        sign: str = "-" if self.isNegative(numerator, denominator) else ""

        n, d = abs(numerator), abs(denominator)

        first_part: int = n // d
        rem: int = n % d

        if rem == 0:
            return sign + str(first_part)

        res = [sign + str(first_part) + "." ]
        seen = {}


        while rem !=0:

            if rem in seen:
                idx: int = seen.get(rem)
                res.insert(idx, "(")
                res.append(")")
                break

            seen[rem] = len(res)
            rem = rem * 10
            temp = (rem) // d
            
            res.append(str(temp))
            rem = rem % d

        return "".join(res)




        
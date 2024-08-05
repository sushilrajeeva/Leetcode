class Solution:
    def getSum(self, a: int, b: int) -> int:

        # Define a mask to simulate 32-bit integer behavior
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        # Iterate till there is no carry  

        while b != 0:
            # carry now contains common
            # set bits of a and b
            carry = a & b

            # Sum of bits of a and b where at
            # least one of the bits is not set
            a = (a ^ b) & MASK

            # Carry is shifted by one so that   
            # adding it to a gives the required sum
            b = (carry << 1) & MASK

        # If a is negative, convert it to a Python negative integer
        return a if a <= INT_MAX else ~(a ^ MASK)
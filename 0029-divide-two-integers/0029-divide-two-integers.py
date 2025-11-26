class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        x = int(float(dividend)/float(divisor))
        if x==2147483648:
            return x - 1
        else:
            return x
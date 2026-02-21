class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count(string):
            c = 0
            for ele in string:
                if int(ele) == 1:
                    c += 1
            return c

        def isPrime(num):
            if num <= 1: return False
            flag = False
            for i in range(2, num):
                if num%i == 0:
                    flag = True
                    break
            return not flag
        prime = 0
        for i in range(left, right+1):
            binn = bin(i)[2:]
            oneCounts = count(binn)
            if isPrime(oneCounts):
                prime += 1
        
        return prime

        
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        print("n", n)
        print("m", m)
        num1: int = self.solve(n, m, True)
        num2: int = self.solve(n, m, False)
        return num1 - num2

    def solve(self, x: int, y: int,flag: bool) -> int:
        total: int = 0
        if flag:
            for i in range(1, x+1):
                if i%y != 0:
                    print(i)
                    total += i
        else:
            for i in range(1, x+1):
                if i%y == 0:
                    total += i
        return total
class Solution:

    def isIncreasing(self, n1: int, n2: int) -> bool:
        if n2 > n1: return True
        return False

    def isSame(self, n1: int, n2: int) -> bool:
        if n1 == n2: return True
        return False

    def isTrionic(self, nums: List[int]) -> bool:
        first = False
        second = False
        third = False
        n = len(nums)

        for i in range(n-1):
            x, y = nums[i], nums[i+1]
            isIncreasing = self.isIncreasing(x, y)
            isSame = self.isSame(x, y)
            if isSame: return False
            print("i", i, "isIncrasing", isIncreasing)
            if not first:
                if not isIncreasing: return False
                first = True
            else:
                if not second:
                    if isIncreasing: continue
                    else:
                        second = True
                else:
                    if not third:
                        if not isIncreasing: continue
                        else:
                            third = True
                    else:
                        if isIncreasing: continue
                        else: return False
        
        return first and second and third




        
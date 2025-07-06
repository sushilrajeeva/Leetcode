class Solution:
    """
        range of m, n -> [0, 1000]
        positive values ? true
        both the individual arrays are alway sorted ? true
        A+B -> C
        can nums1 or nums2 be empty ? yes

        Algo: 
            TC: O(m + n)
            SC: O(m + n)
            create a temp array
            p1, p2 in nums1, nums2
            for i in range(m + n + 1):
                if p1 < m and p2 < n:
                    if nums1[p1] < nums2[p2]:
                        temp[i] = nums1[p1]
                        p1 += 1
                    else:
                        temp[i] = nums2[p2]
                        p2 += 1
                else:
                    if p1 < m:
                        temp[i] = nums1[p1]
                        p1 += 1
                    else:
                        temp[i] = nums2[p2]
                        p2 += 1
            return mid of temp if odd or mean of two mids of temp if even length
                
        
    """

    def simpleMedian(self, nums: List[int]) -> float:
        if not nums: return -1.0
        is_even: int = len(nums) % 2 == 0
        mid: int = len(nums) // 2
        if not is_even:
            return nums[mid]
        
        return (nums[mid] + nums[mid - 1])/2
        

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1: return self.simpleMedian(nums2)
        if not nums2: return self.simpleMedian(nums1)

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m: int = len(A)
        n: int = len(B)

        total: int = m + n
        half: int = (m + n)//2
        low: int = 0
        high: int = m - 1

        is_even: bool = total % 2 == 0

        while True:
            Amid = (low + high) // 2
            Bmid = half - Amid -2

            Aleft = A[Amid] if Amid >= 0 else float("-inf")
            Bleft = B[Bmid] if Bmid >= 0 else float("-inf")
            Aright = A[Amid + 1] if Amid + 1 < m else float("inf")
            Bright = B[Bmid + 1] if Bmid + 1 < n else float("inf")

            # check if we have reached correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if not is_even:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                high = Amid - 1
            else:
                low = Amid + 1
    






        


        

                




        
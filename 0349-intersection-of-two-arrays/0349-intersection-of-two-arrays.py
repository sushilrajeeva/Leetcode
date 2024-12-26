class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n, m = len(nums1), len(nums2)

        buffer: List[int] = [0] * 1001
        res: List[int] = []

        for i in range(n):
            if buffer[nums1[i]] == 0:
                buffer[nums1[i]] += 1
        
        for j in range(m):
            if buffer[nums2[j]] == 1:
                buffer[nums2[j]] = 0
                res.append(nums2[j])

        return res
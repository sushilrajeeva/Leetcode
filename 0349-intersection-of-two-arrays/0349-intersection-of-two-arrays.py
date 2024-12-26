class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1).intersection(set(nums2)))
        
        # n, m = len(nums1), len(nums2)
        # result = []

        # index1, index2 = 0, 0
        
        # freq1 = [0] * (1001)
        # freq2 = [0] * (1001)

        # for i in range(n):
        #     freq1[nums1[i]] += 1
        
        # for j in range(m):
        #     freq2[nums2[j]] += 1

        # for i in range(len(freq1)):
        #     if freq1[i] > 0 and freq2[i] > 0:
        #         result.append(i)

        # return result

        
        
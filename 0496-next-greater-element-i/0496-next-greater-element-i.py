class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashMap = {}
        n1 = len(nums1)
        n2 = len(nums2)

        for index, num in enumerate(nums2):
            hashMap[num] = index

        stack = []

        for i in reversed(range(n2)):
            if not stack:
                stack.append(nums2[i])
                nums2[i] = -1
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if not stack:
                    stack.append(nums2[i])
                    nums2[i] = -1
                else:
                    ele = nums2[i]
                    nums2[i] = stack[-1]
                    stack.append(ele)
        
        for index, num in enumerate(nums1):
            nums1[index] = nums2[hashMap[num]]

        return nums1
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def binaryToNumber(self, nums: str) -> int:
        # number = 0
        # power = len(nums)-1
        # for num in nums:
        #     number += (int(num)*(2**power))
        #     power -= 1
        # return number
        return int(nums, 2)


    

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        binary = ""
        arr: List[str] = []
        def convertToBinary(root: Optional[TreeNode], binary: str, arr: List[str]) -> None:

            if not root:
                return None
            binary += str(root.val)

            if not root.left and not root.right:
                arr.append(binary)
            else:
                convertToBinary(root.left, binary, arr)
                convertToBinary(root.right, binary, arr)

        convertToBinary(root, binary, arr)
        res = 0
        for i in range(len(arr)):
            res += self.binaryToNumber(arr[i])

        return res
        
            
        
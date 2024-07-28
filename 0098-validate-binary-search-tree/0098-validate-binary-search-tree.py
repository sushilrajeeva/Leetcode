# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        left = float("-inf")
        right = float("inf")
        def isValid(root: Optional[TreeNode], left:int , right: int) -> bool:
            if not root:
                return True

    
            if not (left < root.val < right):
                return False
                
            leftOperation = isValid(root.left, left, root.val)
            if not leftOperation:
                return False
            rightOperation = isValid(root.right, root.val, right)
            return leftOperation and rightOperation

        return isValid(root, left, right)

        
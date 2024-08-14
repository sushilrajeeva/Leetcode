# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft: bool = False) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            if isLeft: return root.val
            return 0

        leftVal: int = self.sumOfLeftLeaves(root.left, True)
        rightVal: int = self.sumOfLeftLeaves(root.right)

        return leftVal + rightVal

        

        

        
        
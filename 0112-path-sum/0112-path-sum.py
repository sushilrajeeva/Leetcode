# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        val: int = 0

        if not root:
            return False

        def pathSumTarget(root: Optional[TreeNode], val: int, targetSum: int) -> bool:
            if not root:
                return False

            val += root.val

            if not root.left and not root.right:
                if val == targetSum:
                    return True
                return False

            left = pathSumTarget(root.left, val, targetSum)
            if left:
                return True
            right = pathSumTarget(root.right, val, targetSum)
            return left or right

        return pathSumTarget(root, val, targetSum)
        
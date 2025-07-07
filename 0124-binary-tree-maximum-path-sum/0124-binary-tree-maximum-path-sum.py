# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum: int = float("-inf")

        def helper(node: Optional[TreeNode]) -> int:
            nonlocal maxSum
            if not node:
                return 0
            
            left_operation: int = max(helper(node.left), 0)
            right_operation: int = max(helper(node.right), 0)

            current_sum = node.val + left_operation + right_operation

            maxSum = max(maxSum, current_sum)

            return node.val + max(left_operation, right_operation)

        helper(root)
        return maxSum
            

        
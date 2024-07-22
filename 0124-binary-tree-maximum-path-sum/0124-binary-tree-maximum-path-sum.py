# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        mem = dict()
        maxSum = [float("-inf")]

        def getMaxPath(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            # Recursively get the maximum path sum of left and right subtrees
            leftSum = max(getMaxPath(root.left), 0)  # Only consider positive contributions
            rightSum = max(getMaxPath(root.right), 0)  # Only consider positive contributions

            # Current path sum including the root node
            currentPathSum = root.val + leftSum + rightSum

            # Update the global maximum path sum
            maxSum[0] = max(maxSum[0], currentPathSum)

            # Return the maximum sum of the path that can be extended to parent
            return root.val + max(leftSum, rightSum)
        
        getMaxPath(root)

        return maxSum[0]


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if not root.left and not root.right:
            return root
        
        # recursively flatten left and right subtree
        # post order
        leftTail = self.flatten(root.left)
        rightTail = self.flatten(root.right)

        if root.left:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        return rightTail if rightTail else leftTail

    

    
        
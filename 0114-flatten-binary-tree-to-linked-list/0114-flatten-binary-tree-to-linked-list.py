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
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail if right_tail else left_tail

    

    
        
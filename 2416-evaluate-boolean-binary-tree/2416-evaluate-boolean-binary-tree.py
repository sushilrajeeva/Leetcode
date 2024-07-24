# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return False

        if not root.left and not root.right:
            return root.val == 1
        
        left = self.evaluateTree(root.left) if root.left else False
        right = self.evaluateTree(root.right) if root.right else False

        if root.val == 2: return left or right
        if root.val == 3: return left and right

        return False
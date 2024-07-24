# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val

        if total == root.val:
            return True
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode])-> bool:

        if not root1 and not root2:
            return True

        if root1 and not root2: return False
        if root2 and not root1: return False

        if root1.val != root2.val:
            return False

        left = self.isMirror(root1.left, root2.right)
        right = self.isMirror(root1.right, root2.left)

        return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.isMirror(root.left, root.right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        val: int = root.val

        def isUnival(root: Optional[TreeNode], val: int) -> bool:

            if not root:
                return True

            if root.val != val:
                return False

            left = isUnival(root.left, val)
            if not left:
                return False
            right = isUnival(root.right, val)

            return left and right

        return isUnival(root, val)

        


        
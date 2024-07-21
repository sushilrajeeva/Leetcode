# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedElements(self, root: Optional[TreeNode], result: List[int]) -> None:

        if not root:
            return

        # Inorder :-> moving left then middle then right
        self.sortedElements(root.left, result)
        result.append(root.val)
        self.sortedElements(root.right, result)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result = []
        self.sortedElements(root, result)
        return result[k-1]




        
        
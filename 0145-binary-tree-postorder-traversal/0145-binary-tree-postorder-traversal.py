# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []

        def postOrder(root: Optional[TreeNode], result: List[int]) -> None:

            if not root:
                return

            postOrder(root.left, result)
            postOrder(root.right, result)
            result.append(root.val)

            return

        postOrder(root, result)

        return result

        
        
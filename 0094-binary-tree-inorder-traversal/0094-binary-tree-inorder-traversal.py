# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(root: Optional[TreeNode], output: List[int]):
            if not root:
                return
            inorder(root.left, output)
            output.append(root.val)
            inorder(root.right, output)

        output = []
        inorder(root, output)
        return output
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            PreOrder = Root -> Left -> Right
            Inorder = Left -> Root -> Right
            PostOrder = Left -> Right -> Root
        """

        if not preorder or not inorder:
            return None

        # Create a dictionary to store the index of each value in inorder traversal for quick lookup
        inorder_index = {value: index for index, value in enumerate(inorder)}

        def build(pre_left: int, pre_right: int, in_left: int, in_right: int) -> TreeNode:
            if pre_left > pre_right or in_left > in_right:
                return None

            # The first value in the current preorder is the root
            root = TreeNode(preorder[pre_left])

            # Finding the index of the root in inorder
            mid = inorder_index[root.val]

            # calculating left size of the left subtree
            left_tree_size = mid - in_left

            # Recursively build the left and right subtrees
            root.left = build(pre_left+1, pre_left + left_tree_size, in_left, mid-1)
            root.right = build(pre_left + left_tree_size + 1, pre_right, mid + 1, in_right)

            return root

        return build(0, len(preorder)-1, 0, len(inorder)-1)
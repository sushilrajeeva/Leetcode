# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxHeight = [0]
        mem = dict()

        def getMaxHeight(root, mem, maxHeight) -> int:

            if not root:
                return 0

            if root in mem:
                return mem[root]

            leftHeight = getMaxHeight(root.left, mem, maxHeight)
            rightHeight = getMaxHeight(root.right, mem, maxHeight)

            mem[root] = max(leftHeight, rightHeight) + 1
            maxHeight[0] = max(maxHeight[0], leftHeight + rightHeight)
            return mem[root]

        getMaxHeight(root, mem, maxHeight)

        return maxHeight[0]

        
        
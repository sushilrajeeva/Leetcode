# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getLowest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        while root.left:
            root = root.left
        return root

    def delete(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        if root.val < key:
            root.right = self.delete(root.right, key)
        elif root.val > key:
            root.left = self.delete(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # if root has both left and right then i need to swap the lowest value from root.right subtree and go to root.right sub tree and delete root.right
            lowest = self.getLowest(root.right)
            root.val = lowest.val
            root.right = self.delete(root.right, lowest.val)

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.delete(root, key)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        path: str = ""
        result = []

        def getPath(root: Optional[TreeNode], path: int, result: List[str]) -> None:

            if not root:
                return None

            if not root.left and not root.right:
                path += str(root.val)
                result.append(path)
                return None

            path += str(root.val) +"->"

            getPath(root.left, path, result)
            getPath(root.right, path, result)

            return

        getPath(root, path, result)

        return result

            
            

        
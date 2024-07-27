# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # Preorder
        string: List[str] = []
        def toString(root: Optional[TreeNode]) -> None:
            if not root:
                string.append("N")
                return

            string.append(str(root.val))
            toString(root.left)
            toString(root.right)
            return

        toString(root)

        return ",".join(string)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        arr = data.split(",")
        self.i = 0

        def dfs():
            if arr[self.i] == "N":
                self.i += 1
                return None

            node: Optional[TreeNode] = TreeNode(int(arr[self.i]))
            self.i += 1
            
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
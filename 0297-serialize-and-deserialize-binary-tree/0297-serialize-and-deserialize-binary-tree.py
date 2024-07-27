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

        # i will perform a preorder traversal and as i go i store the node in a list 
        # if i encounter None then i will store N in its place
        # at the end i will return the string by coverting the list to string by using join and using ',' as a delimiter

        string: List[str] = []

        def preorder(root: Optional[TreeNode]) -> None:

            if not root:
                string.append("N")
                return

            string.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            return

        preorder(root)

        return ",".join(string)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # I know that the seralization is in inorder and where ever N is present that means it is end of the node
        # i will convert string to list by splitting it by ','
        arr: List[str] = data.split(",")
        # will create a global index counter to keep track of which node i am currently in
        self.i = 0
        
        # Recursively construct the Binary Tree and return the root
        def dfs() -> Optional[TreeNode]:

            # if i reach N then i must return None
            if arr[self.i] == "N":
                self.i += 1
                return None
            
            # if arr[self.i] != 'N' then i must create a node of value arr[self.i]
            node: Optional[TreeNode] = TreeNode(arr[self.i])
            self.i += 1

            # recursively use this function to build the left and right subtrees -> self.i is global so it takes care of counter or index position of the arr
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
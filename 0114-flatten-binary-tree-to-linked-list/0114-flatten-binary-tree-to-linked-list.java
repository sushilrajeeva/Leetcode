/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public TreeNode flat(TreeNode root){
        if (root == null){
            return null;
        }

        if (root.left == null && root.right == null){
            return root;
        }

        TreeNode left = flat(root.left);
        TreeNode right = flat(root.right);

        if (left != null){
            left.right = root.right;
            root.right = root.left;
            root.left = null;
        }

        if (right != null){
            return right;
        }
        return left;
    }

    public void flatten(TreeNode root) {

        flat(root);
        
    }
}
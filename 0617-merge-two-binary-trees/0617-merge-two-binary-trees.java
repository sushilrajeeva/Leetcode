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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {

        if (root1 == null && root2 == null){
            return null;
        }

        int v1 = 0;
        int v2 = 0;

        TreeNode left1 = null;
        TreeNode right1 = null;
        TreeNode left2 = null;
        TreeNode right2 = null;

        if (root1 != null){
            v1 = root1.val;
            left1 = root1.left;
            right1 = root1.right;
        }
        if (root2 != null){
            v2 = root2.val;
            left2 = root2.left;
            right2 = root2.right;
        }

        TreeNode root = new TreeNode(v1+v2);

        root.left = mergeTrees(left1, left2);
        root.right = mergeTrees(right1, right2);

        return root;
        
    }
}
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

    public int travel(TreeNode root, int cal) {
        if (root == null) {
            return 0;
        }

        cal = cal * 2 + root.val;

        int left = travel(root.left, cal);
        int right = travel(root.right, cal);

        if (root.left == null && root.right == null) {
            return cal;
        }

        return left + right;
    }

    public int sumRootToLeaf(TreeNode root) {

        int total = 0;
        return travel(root, total);
        
    }
}
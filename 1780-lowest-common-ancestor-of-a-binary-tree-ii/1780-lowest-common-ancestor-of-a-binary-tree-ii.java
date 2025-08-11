/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {

    public TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode left = lca(root.left, p, q);
        TreeNode right = lca(root.right, p, q);

        if (left != null && right != null) {
            return root;
        }

        return (left != null) ? left : right;
    }

    public boolean dfs(TreeNode node, TreeNode target) {
        // Base Case: Target found
        if (node == target) {
            return true;
        }

        // Base Case: Reached null, target not found
        if (node == null) {
            return false;
        }

        // Recursive Case: Search target in left or right subtree
        boolean left = dfs(node.left, target);
        if (left) {
            return left;
        }
        return dfs(node.right, target);
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        // Step 1: find the LCA
        TreeNode node = lca(root, p, q);

        // Step 2: check if LCA is P or Q, then check if the other is in its subtree
        TreeNode target = (node == p) ? q : p;

        return dfs(node, target) ? node : null;

        
    }
}
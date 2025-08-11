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

    private Set<TreeNode> targetNodes;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {

        if (root == null) {
            return null;
        }

        targetNodes = new HashSet<>();
        for (TreeNode node : nodes) {
            targetNodes.add(node);
        }

        return findLCA(root);

    }

    private TreeNode findLCA(TreeNode root) {
        if (root == null) {
            return null;
        }
        if (this.targetNodes.contains(root)) {
            return root;
        }

        TreeNode left = findLCA(root.left);
        TreeNode right = findLCA(root.right);

        if (left != null && right != null) {
            return root;
        }

        return (left != null) ? left : right;
    }
}
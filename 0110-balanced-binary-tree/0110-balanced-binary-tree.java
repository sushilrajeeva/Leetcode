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

import static java.lang.Math.*;

class Solution {

    public int getHeight(TreeNode root){
        if (root == null){
            return 0;
        }

        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);

        if(leftHeight == -1 || rightHeight == -1){
            return -1;
        }

        if(abs(leftHeight - rightHeight) > 1){
            return -1;
        }

        return max(leftHeight, rightHeight) + 1;
    }

    public boolean isBalanced(TreeNode root) {

        if (getHeight(root) == -1){
            return false;
        }
        return true;
        
    }
}
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
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {

        if (original == null){
            return null;
        }

        if (original.val == target.val){
            return cloned;
        }

        final TreeNode left = getTargetCopy(original.left, cloned.left, target);
        final TreeNode right = getTargetCopy(original.right, cloned.right, target);

        if (left!=null){
            return left;
        }
        if (right!=null){
            return right;
        }

        return null;
        
    }
}
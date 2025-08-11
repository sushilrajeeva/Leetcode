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
    public List<List<Integer>> verticalOrder(TreeNode root) {

        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }

        Map<Integer, ArrayList> memo = new HashMap<>();
        int left = 0;
        int right = 0;

        Queue<Pair<TreeNode, Integer>> q = new ArrayDeque();
        q.offer(new Pair(root, 0));

        while (!q.isEmpty()) {
            Pair<TreeNode, Integer> pair = q.poll();
            TreeNode node = pair.getKey();
            Integer col = pair.getValue();

            if (!memo.containsKey(col)) {
                memo.put(col, new ArrayList<Integer>());
            }
            memo.get(col).add(node.val);
            left = Math.min(left, col);
            right = Math.max(right, col);

            if (node.left != null) {
                q.offer(new Pair(node.left, col - 1));
            }
            if (node.right != null) {
                q.offer(new Pair(node.right, col + 1));
            }
        }

        for (int i = left; i <= right; i++) {
            if (memo.containsKey(i)) {
                res.add(memo.get(i));
            }
        }

        return res;
        
    }
}
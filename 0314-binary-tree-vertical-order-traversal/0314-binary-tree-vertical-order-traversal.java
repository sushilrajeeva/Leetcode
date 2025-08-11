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

class Item {
    TreeNode node;
    int col;
    Item(TreeNode node, int col) {
        this.node = node;
        this.col = col;
    }
}

class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {

        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }

        Map<Integer, ArrayList> memo = new HashMap<>();
        int left = 0;
        int right = 0;

        Queue<Item> q = new ArrayDeque();
        q.offer(new Item(root, 0));

        while (!q.isEmpty()) {
            Item item = q.poll();
            TreeNode node = item.node;
            Integer col = item.col;

            if (!memo.containsKey(col)) {
                memo.put(col, new ArrayList<Integer>());
            }
            memo.get(col).add(node.val);
            left = Math.min(left, col);
            right = Math.max(right, col);

            if (node.left != null) {
                q.offer(new Item(node.left, col - 1));
            }
            if (node.right != null) {
                q.offer(new Item(node.right, col + 1));
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
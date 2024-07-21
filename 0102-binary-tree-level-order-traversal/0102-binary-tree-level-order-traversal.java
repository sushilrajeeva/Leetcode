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
import java.util.ArrayList;
import java.util.List;

class Que {
    private ArrayList<TreeNode> queue;

    // Default constructor
    public Que(){
        this.queue = new ArrayList<>();
    }

    // Parameterized constructor
    public Que(ArrayList<TreeNode> queue){
        this.queue = queue;
    }

    public boolean isEmpty(){
        return this.queue.size() == 0;
    } 

    public TreeNode peak(){
        if(!this.isEmpty()){
            return this.queue.get(0);
        } else {
            return null; // Return null if the queue is empty
        }
    }

    public void enqueue(TreeNode node){
        this.queue.add(node);
    }

    public TreeNode dequeue(){
        if(!this.isEmpty()){
            return this.queue.remove(0);
        } else {
            return null; // Return null if the queue is empty
        }
    }
}

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        if(root == null){
            return new ArrayList<>();
        }

        List<List<Integer>> result = new ArrayList<>();

        Que queue = new Que();
        queue.enqueue(root);
        queue.enqueue(null);
        result.add(new ArrayList<>());

        while(!queue.isEmpty()){
            TreeNode currentNode = queue.dequeue();

            if (currentNode == null){
                if (!queue.isEmpty()){
                    result.add(new ArrayList<>());
                    queue.enqueue(null);
                }
            }else{
                result.get(result.size() - 1).add(currentNode.val);

                if(currentNode.left != null){
                    queue.enqueue(currentNode.left);
                }
                if(currentNode.right != null){
                    queue.enqueue(currentNode.right);
                }
                
            }
        }

        if (result.get(result.size()-1).size() == 0){
            result.remove(result.size()-1);
        }
        
        return result;
        
    }
}
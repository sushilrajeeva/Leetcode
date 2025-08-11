/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {

        Node a = p;
        Node b = q;

        int switchedA = 0;
        int switchedB = 0;

        while (a != b) {
            if (a == null) {
                a = q;
                switchedA += 1;
                if (switchedA > 1) {
                    return null;
                }
            } else {
                a = a.parent;
            }

            if (b == null) {
                b = p;
                switchedB += 1;
                if (switchedB > 1) {
                    return null;
                }
            } else {
                b = b.parent;
            }
        }

        return a;
        
    }
}
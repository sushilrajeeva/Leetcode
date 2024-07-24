/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool checkTree(TreeNode* root) {

        if (root == NULL){
            return false;
        }

        long total = 0;

        if (root->left != NULL){
            total += root->left->val;
        }
        if(root->right != NULL){
            total += root->right->val;
        }

        if (root->val == total){
            return true;
        }

        return false;
        
    }
};
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {

        if (original==NULL){
            return NULL;
        }

        if (original->val == target->val){
            return cloned;
        }

        TreeNode* left = getTargetCopy(original->left, cloned->left, target);

        if (left != NULL){
            return left;
        }

        TreeNode* right = getTargetCopy(original->right, cloned->right, target);
        if (right != NULL){
            return right;
        }

        return NULL;
        
    }
};
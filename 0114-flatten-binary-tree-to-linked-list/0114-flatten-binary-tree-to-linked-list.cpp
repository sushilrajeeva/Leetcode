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

    TreeNode* flat (TreeNode* root) {
        if (root == NULL){
            return NULL;
        }
        if (root->left == NULL && root->right == NULL){
            return root;
        }

        TreeNode* left = flat(root->left);
        TreeNode* right = flat(root->right);

        if (left != NULL){
            left->right = root->right;
            root->right = root->left;
            root->left = NULL;
        }
        if (right != NULL) {
            return right;
        }

        return left;
    }

    void flatten(TreeNode* root) {
        flat(root);
    }
};
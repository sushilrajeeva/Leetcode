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

#include <iostream>
#include <algorithm>

using std::max;
using std::abs;

class Solution {
public:

    int getHeight(TreeNode* root){
        if (root == NULL){
            return 0;
        }

        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);

        if(leftHeight == -1 || rightHeight == -1){
            return -1;
        }

        if(abs(leftHeight - rightHeight) > 1){
            return -1;
        }

        return max(leftHeight, rightHeight) + 1;
    }

    bool isBalanced(TreeNode* root) {
        if(getHeight(root) == -1){
            return false;
        }
        return true;
    }
};
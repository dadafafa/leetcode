class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int Traversal(TreeNode *root, int &maxpath){
        if(root == NULL){
            return 0;
        }
        int mid = root->val;
        int left = Traversal(root->left, maxpath);
        int right = Traversal(root->right, maxpath);
        maxpath = max(maxpath, mid+left+right);
        maxpath = max(maxpath, mid+left);
        maxpath = max(maxpath, mid+right);
        maxpath = max(maxpath, mid);
        int res = max(left, right);
        res += mid;
        return res;
        
    }
    
    int maxPathSum(TreeNode * root) {
        // write your code here
        int max = INT_MIN;
        Traversal(root, max);
        return max;
        
    }
};

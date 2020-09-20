class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None
        if root.val == A.val or root.val == B.val:
            return root
        left = self.lowestCommonAncestor(root.left,A,B)
        right = self.lowestCommonAncestor(root.right,A,B)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None

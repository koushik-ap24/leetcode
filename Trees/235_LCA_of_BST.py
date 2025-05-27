# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):
            # Base case - if node is equal to p or q it is immediately the lowest ancestor!
            if node.val == p.val or node.val == q.val:
                return node
            
            pSearch = node.left if node.val > p.val else node.right
            qSearch = node.left if node.val > q.val else node.right
            # If there is a split (nodes are in opposite subtrees), then this is the LCA
            if pSearch != qSearch:
                return node
            
            # Otherwise continue to the subtree that has both values
            return dfs(pSearch)
        
        return dfs(root)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal
        # Maintain array for this traversal order
        # If current node is <= the last added node, then invalid BST
        traversal = []
        def dfs(node):
            if not node:
                return True
            
            # Check if left subtree is valid
            if not dfs(node.left) or (traversal and node.val <= traversal[-1]):
                return False

            traversal.append(node.val)

            # If left subtree is valid, the this root's subtree is only valid if its right subtree is valid
            return dfs(node.right)
        
        return dfs(root)

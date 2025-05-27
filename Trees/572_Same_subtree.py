from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
# The issue is that the dfs is trying to do two things at once:
#  - Traverse the tree to find a match for subRoot.
#  - If node.val == subnode.val, try to verify if the subtree matches.
# This leads to incorrect behavior.  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node, subnode):
            if node is None and subnode is None:
                return True
            
            if node is None or subnode is None:
                return False
            
            left = right = False

            if node.val == subnode.val:
                left = dfs(node.left, subnode.left)
                right = dfs(node.right, subnode.right)
                print(f"{node.val}: {left and right} {node.val} {subnode.val}")
                return left and right
            else:
                left = dfs(node.left, subnode)
                right = dfs(node.right, subnode)
                print(f"{node.val}: {left or right} {node.val} {subnode.val}")
                return left or right
        
        return dfs(root, subRoot)

        ## Good approach -> split into two helper functions
        ## One to traverse tree, 
        ## one to check if subtree starting at node is the same as subroot
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        return False
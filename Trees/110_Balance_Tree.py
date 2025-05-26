from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ## Check for maxHeight and balance in the same traversal instead of seperate
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        def checkBalance(node):
            if node is None:
                return (0,True)
            
            resLeft = checkBalance(node.left)
            resRight = checkBalance(node.right)
            if not (resLeft[1] and resRight[1]) or abs(resLeft[0]-resRight[0]) > 1:
                return (1 + max(resLeft[0], resRight[0]), False)
            
            return (1 + max(resLeft[0], resRight[0]), True)

        
        res = checkBalance(root)
        return res[1]
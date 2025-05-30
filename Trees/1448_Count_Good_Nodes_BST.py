from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Constraints:
        # tree is non empty
        # tree can contain duplicate nodes
        # a good node must be greater than or equal to the nodes taken to get to it from root

        # Approach:
        # Maintain max recStack for the path to the current node
        maxRecStack = deque([])
        # Traverse the tree in pre-order via dfs
        def dfs(node):
            if not node:
                return 0
    
            # When processing node, check if the max in recStack < node.val.
            res = 0
            if not maxRecStack or maxRecStack[-1] <= node.val:
                res += 1
                maxRecStack.append(node.val)
            else:
                maxRecStack.append(maxRecStack[-1])
            
            # process left and right subtrees
            res += dfs(node.left) + dfs(node.right)
            maxRecStack.pop()
            return res
            
        # Return the result
        return dfs(root)
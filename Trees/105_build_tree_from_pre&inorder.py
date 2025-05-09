from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC = O(n) -> process each node at most once.
# SC = O(n) -> at most make n recursive calls.
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Create hashmap for in-order
        treeMap = {}
        for i in range(len(inorder)):
            treeMap[inorder[i]] = i
        
        # Cleaner way to convert array to hashmap
        treeMap = {value: idx for idx, value in enumerate(inorder)}
        
        self.pre_index = 0
        def dfs(l, r):
            if l > r:
                return None
            # pre-order is the order we use to create the tree.
            # In-order allows us to separate the left and right subtrees for that node.
            val = preorder[self.pre_index]
            node = TreeNode(val) # create the root node
            self.pre_index += 1
            split = treeMap.get(val)

            # recursively build the left and right subtrees
            node.left = dfs(l, split-1)
            node.right = dfs(split+1, r)

            return node
        
        return dfs(0, len(inorder)-1)

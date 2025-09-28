from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Initialize a deque for BFS, storing (node, index).
        # The root is given the arbitrary starting index of 1.
        queue = deque([(root, 1)])
        max_width = 0

        while queue:
            level_size = len(queue)
            _, level_start_index = queue[0] 
            level_end_index = 0
            
            for _ in range(level_size):
                node, index = queue.popleft()
                level_end_index = index 

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))
            
            # The width of the current level is (Rightmost Index - Leftmost Index + 1)
            current_width = level_end_index - level_start_index + 1
            max_width = max(max_width, current_width)

        return max_width
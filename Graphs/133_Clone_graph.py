
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        oldToNew = {}
        queue = deque([node])
        oldToNew[node] = Node(node.val)
        res = None

        while queue:
            node = queue.popleft()
            copy = oldToNew[node]
            if not res:
                res = copy
    
            for neighbour in node.neighbors:
                # Only create new node if it hasnt been visited yet
                if neighbour not in oldToNew:
                    oldToNew[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                # Otherwise just add it as neighbour to current node
                copy.neighbors.append(oldToNew[neighbour])
        
        return res
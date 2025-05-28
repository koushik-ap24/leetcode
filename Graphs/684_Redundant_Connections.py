from collections import defaultdict
from typing import List


class Solution:
    # Optimal DFS Solution
    # TC (O(V+E)) # SC (O(V+E))

    # Can be further optimised using Union Find!
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ## Build graph
        edgesMap = {}
        graph = defaultdict(list)
        for i in range(len(edges)):
            src = edges[i][0]
            dest = edges[i][1]
            graph[src].append(dest)
            graph[dest].append(src)
            edgesMap[(src,dest)] = i
        
        visited = set()
        resIdx = 0
        # Keep track of where the cycle starts, as we dont want to consider nodes neighbouring to cycleStart that are not part of cycle.
        cycleStart = -1
        def dfs(node, parent):
            nonlocal resIdx
            nonlocal cycleStart

            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour != parent:
                    if dfs(neighbour, node):
                        if cycleStart != -1:
                            idx = edgesMap[(node, neighbour)] if (node,neighbour) in edgesMap else edgesMap[(neighbour,node)]
                            resIdx = max(resIdx, idx)
                            print([node, neighbour])
                        
                        if cycleStart == node:
                            cycleStart = -1
                        
                        return True

            return False
        
        dfs(1,None)
        return edges[resIdx]
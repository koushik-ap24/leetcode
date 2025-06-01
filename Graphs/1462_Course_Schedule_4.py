from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build graph
        graph = {i: [] for i in range(numCourses)}
        cache = {}
        for src,dest in prerequisites:
            graph[src].append(dest)
            cache[(src,dest)] = True
        
        ## Approach: DFS Path Finding with Memoization
        # Path finding with dp for more efficient lookups
        def dfs(node, target):
            if node == target:
                return True
            
            if (node,target) in cache:
                return cache[(node,target)]
            
            for neighbour in graph[node]:
                if dfs(neighbour, target):
                    cache[(node,target)] = True
                    return True
            
            cache[(node,target)] = False
            return False
        
        res = []
        for src,target in queries:
            res.append(dfs(src,target))
        
        return res
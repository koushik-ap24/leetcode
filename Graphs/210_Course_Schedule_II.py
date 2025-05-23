from typing import List


class Solution:
    ## Topological sort with cycle detection
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Solution 1, use DFS to find cycle
        # If no cycle, return the visited nodes in reverse order (as you will process dependencies after parent, so DFS will add dependencies first to result when recursing back up the stack)
        
        ## Build graph
        graph = {i : [] for i in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        ## Use DFS to check for cycle
        visited = set()
        recStack = set()
        res = []

        def dfs(node):
            if node in recStack:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)
            recStack.add(node)

            for neighbour in graph.get(node, []):
                if dfs(neighbour):
                    return True
            
            recStack.remove(node)
            res.append(node)
            return False
        
        ## Iterate through nodes and find the cycle
        for node in graph:
            if node not in visited:
                # Return [] if a cycle is detected
                if dfs(node):
                    return []
        
        # If no cycles, then courses are valid, therefore true
        res.reverse()
        return res

        #######################################################################
        ## Solution 2 - use Kahn's algorithm for topological sort
        graph = {i : [] for i in range(numCourses)}
        inDegree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            inDegree[dest] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        zeroCount = 0
        res = []
        while queue:
            zeroCount += 1
            node = queue.popleft()
            res.append(node)
            for neighbour in graph[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if zeroCount != numCourses:
            return []
        else:
            return res        
        
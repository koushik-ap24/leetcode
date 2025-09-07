from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Approach: BFS with shortest path storage
        # Because this is unweighted, we can use BFS instead of Dijkstra
        # TC: O(q * (v + e)), SC: O(v + e) for graph storage

        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        res = []
        for src, dest in queries:
            if src not in graph or dest not in graph:
                # Edge cases
                res.append(float(-1))
                continue
            
            if src == dest:
                res.append(float(1))
                continue
            
            # Standard BFS with parent and visited node tracking
            # Parent tracking allows us to backtrack the path once we reach the destination
            parent = defaultdict(str)
            visited = set()
            queue = deque([])
            queue.append(src)
            parent[src] = (-1, -1)
            visited.add(src)

            while queue:
                node = queue.popleft()
                for neighbour, weight in graph[node]:
                    if neighbour not in visited: # Unvisited node
                        parent[neighbour] = (node, weight)
                        visited.add(neighbour)
                        queue.append(neighbour)
            
            if dest not in visited:
                res.append(float(-1))
                continue
            
            # Backtrack to get the edges and multiply the weights to the answer
            answer = 1
            current = dest
            while parent[current] != (-1, -1):
                nextNode, value = parent[current]
                answer *= value
                current = nextNode
            
            res.append(answer)

        return res
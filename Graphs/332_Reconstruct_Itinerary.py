from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## Realise this problem requires us to use each edge exactly once, and visit all vertices.
        # So construct a path using each edge covering all vertices - definition of **Euler path**
        # Algorithm to find Euler path - Hierholzer's Algorithm.
        # Use heap to ensure lexical order of the path.
        # TC: O(E log E), SC: O(E)
        graph = defaultdict(list)
        for src,dest in tickets:
            heapq.heappush(graph[src], dest)
        
        res = []
        def dfs(curr):
            while graph[curr]:
                nextDest = heapq.heappop(graph[curr])
                dfs(nextDest)
            res.append(curr)
        
        dfs("JFK")
        res.reverse()
        return res
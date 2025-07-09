from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ## Unweighted graph -> min cost to connect all vertices problem
        # Need to make a MST using Prim's/Kruskal
        # This implementation uses Prim's
        # TC: O(n^2) + O((n^2)logn), SC: O(n^2)

        # Create edge array
        # Format: ((x_d, y_d), weight)
        graph = defaultdict(list)
        for i in range(len(points)):
            x_s, y_s = points[i]
            for j in range(i+1, len(points)):
                x_d, y_d = points[j]
                weight = abs(x_s - x_d) + abs(y_s - y_d)
                graph[(x_s, y_s)].append((weight, (x_d, y_d)))
                graph[(x_d, y_d)].append((weight, (x_s, y_s)))
        
        # graph = {(1,1): [((2,1),3), ((3,3), 10)]}
        # Prim's Algo
        pq = []
        visited = set()
        minCost = 0
        # start with the first point
        pq.append((0, tuple(points[0])))
        while pq:
            weight, point = heapq.heappop(pq)
            if point in visited:
                continue
            
            visited.add(point)
            minCost += weight
            for neighbour in graph[point]:
                if neighbour[0] not in visited:
                    heapq.heappush(pq, neighbour)
        
        return minCost

from collections import defaultdict
import heapq
import math
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialise Graph
        graph = defaultdict(list)
        for src,dest,time in times:
            graph[src].append((dest, time))

        # Run Dijkstra's algorithm
        distances = {}
        distances[k] = 0
        distanceQueue = [(0, k)]

        while distanceQueue:
            currDistance, currNode = heapq.heappop(distanceQueue)

            # Dont consider if a shorter path has already been found
            if currDistance > distances.get(currNode, math.inf):
                continue
            
            for neighbour, weight in graph[currNode]:
                distance = weight + currDistance

                if distance < distances.get(neighbour, math.inf):
                    distances[neighbour] = distance
                    heapq.heappush(distanceQueue, (distance, neighbour))
        
        # Return the max distance from the source
        return -1 if len(distances) < n else max(distances.values())
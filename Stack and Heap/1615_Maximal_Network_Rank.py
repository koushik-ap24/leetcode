import heapq
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ## Approach: Graph + Heap
        ## Intuition: We can use a max heap to keep track of the nodes with the highest degree
        ## and then check the pairs of nodes with the highest degree to see if they are directly connected
        ## If they are directly connected, we subtract 1 from the rank
        # TC: O(nlogn + m) where n is number of nodes and m is number of edges
        # SC: O(n + m) for the edge set and heap
        
        edgeCount = [(0,i) for i in range(n)]
        edgeSet = set()

        # Track incident edges for each node
        for src, dest in roads:
            edgeSet.add((src,dest))
            edgeCount[src] = (edgeCount[src][0] - 1, src)
            edgeCount[dest] = (edgeCount[dest][0] - 1, dest)

        res = 0
        heapq.heapify(edgeCount)
        topCount, topNode = heapq.heappop(edgeCount)
        topNodes = [topNode]
        print(edgeCount)

        while len(edgeCount):
            count, node = heapq.heappop(edgeCount)
            
            for candidate in topNodes:
                rank = -topCount - count

                # check for edge
                if (node, candidate) not in edgeSet and (candidate, node) not in edgeSet:
                    return max(rank, res)
                else:
                    rank -= 1
                
                if rank < res:
                    return res
            
                res = max(res, rank)

            if count == topCount:
                topNodes.append(node)
        
        return res

            

from collections import defaultdict, deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([(0, 0)])
        maxTime = 0

        while queue:
            node, level = queue.popleft()

            if node in visited:
                continue

            visited.add(node)
            rtt = 2*level
            if rtt <= patience[node]:
                lastPacketTime = 0
            else:
                lastPacketTime = ((rtt-1)//patience[node]) * patience[node]
            
            maxTime = max(maxTime, lastPacketTime + rtt)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))

        return maxTime + 1
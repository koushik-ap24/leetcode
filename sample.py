import heapq
from typing import Counter

s = [[1,4],[2,4],[1,2]]
s.sort(key=lambda i:i[1])

print(s)

s = "ccdsjcnjdscuewiaaaaa"
maps = Counter(s)
print(maps)

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("DFS traversal starting from node 'A':")
dfs(set(), graph, 'A')

from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

print("BFS traversal starting from node 'A':")
bfs(graph, 'A')

arr = [(0,1),(0,2), (0,4)]
t1 = tuple(arr)
s = set()
s.add(t1)

arr2 = [(0,4),(0,1),(0,2)]
t2 = tuple(arr2)
print(t2 in s)

s = [[1,4],[2,4],[0,2]]
heapq.heapify(s)
while s:
  print(heapq.heappop(s))
  
reserve = None

###############
res = [[] for _ in range(5)]
res[3].append(50)
res[1].append(-1)
print(res)

import bisect

def rightmost_leq(arr, target):
    idx = bisect.bisect_right(arr, target)
    return idx - 1 if idx > 0 else -1

arr = [1,2,3,4,5]
target = 1
print(rightmost_leq(arr, target))
from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incidentEdges = defaultdict(int)
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                incidentEdges[recipes[i]] += 1

        res = []
        queue = deque()
        for i in range(len(supplies)):
            queue.append(supplies[i])

        while queue:
            node = queue.popleft()
            for i in graph[node]:
                incidentEdges[i] -= 1
                if incidentEdges[i] == 0:
                    queue.append(i)
                    res.append(i)
                    
        return res
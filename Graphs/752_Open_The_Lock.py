from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ## Approach:
        # Decision tree with BFS traversal instead of DFS
        # Not DP since we will never revisit a decision again
        # Starting at "0000", we can calculate all of its children that can be achieveed in one move
        # Do that for all childrens until we reach the target
        # Each BFS "level" is the number of moves, and BFS guarantees shortest path
        
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque([("0000", 0)])
        visit = set(deadends)

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))
        return -1
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ## Approach: Find all candidate starting positions in s that match the first character of goal
        # Then, for each candidate, check if rotating s from that position matches goal
        ## TC: O(n^2) in worst case, SC: O(1)
        if len(s) != len(goal):
            return False
        
        n = len(s)
        candidates = set()
        # Get candidate starting positions
        for i in range(n):
            if s[i] == goal[0]:
                candidates.add(i)
        
        for start in candidates:
            i = start
            j = 0
            while j < n:
                if s[i] != goal[j]:
                    break
                i = (i + 1) % n
                j += 1
            
            if j == n:
                return True
        
        return False
        
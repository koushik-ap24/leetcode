from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        ## Approach: Stack based
        # The stack will hold the canonical path
        # Split by "/" to get path components and deal with multi slashes
        # If component is "." -> do nothing
        # TC: O(n), SC: O(n)

        
        # Filter out empty (multi slashes) strings
        components = [c for c in path.split("/") if c]

        parent = deque([])
        for component in components:
            if component == "..":
                if len(parent) > 0:
                    parent.pop()
            elif component != ".":
                parent.append("/" + component)
        
        if len(parent) == 0:
            return "/"

        res = ""
        while parent:
            res += parent.popleft()
        
        return res



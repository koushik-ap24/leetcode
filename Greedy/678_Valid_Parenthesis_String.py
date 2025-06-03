from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        ## Approach: Greedy with Two Stacks
        # Use two stacks to track the indices of '(' and '*'
        # If we encounter a ')', we pop from the '(' stack if available, otherwise from the '*' stack
        # At the end, if we find a '(' appears before a '*', we return False

        stack = deque([])
        starStack = deque([])

        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stack.append(i)
            elif ch == "*":
                starStack.append(i)
            else:
                if not stack and not starStack:
                    return False
                
                stack.pop() if stack else starStack.pop()
        
        if len(stack) <= len(starStack):
            while stack and starStack:
                openIdx, starIdx = stack.pop(), starStack.pop()
                if openIdx > starIdx:
                    return False
            
            return True
            
        return False
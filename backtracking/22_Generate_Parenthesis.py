from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking solution
        # impose condition for '('
        # keep track of the index of the outermost "("

        # Initial approach, use stack to keep track of open braces and only pop when a close brace is added
        # Did not work as intended
        # logic for '(' handling is too complicated
        res = []
        combination = []
        m = 2*n
        stack = deque([])

        def dfs(i, start):
            if len(combination) == m:
                res.append(''.join(combination))
                return
            

            if len(stack) < int((m-start)/2):
                stack.append("(")
                combination.append("(")
                print(stack)
                newStart = i if len(stack) == 1 else start
                print(f"start: {start}")
                print(f"newStart: {newStart}")
                dfs(i+1, newStart)
                combination.pop()
                

            if i != 0 and len(stack) > 0:
                stack.pop()
                combination.append(")")
                dfs(i+1, start)
                combination.pop()
        
        dfs(0,0)
        return res
    
        ## Better approach - simpler backtracking
        # Just keep track of number of open and close brackets in combination
        # If open < n, then add open brace
        # If close < open, then add close brace
        # if number of brackets (open + close) == n, then we have found valid combination
        res = []
        combination = []

        def dfs(open, close):
            if open + close == 2*n:
                res.append(''.join(combination))
                return
            
            if open < n:
                combination.append("(")
                dfs(open+1, close)
                combination.pop()   

            if close < open:
                combination.append(")")
                dfs(open, close+1)
                combination.pop()
        
        dfs(0,0)
        return res
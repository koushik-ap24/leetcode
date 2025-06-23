from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        ## Approach: Use two stacks to keep track of the current number and string.
        # TC: O(n), SC: O(n)
        currstr = ""
        currNum = 0
        numStack = deque([])
        stringStack = deque([])

        for i in range(len(s)):
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
            elif s[i] == "[":
                numStack.append(currNum)
                stringStack.append(currstr)

                currstr = ""
                currNum = 0
            elif s[i] == "]":
                prevstr, repnum = stringStack.pop(), numStack.pop()
                currstr = prevstr + (repnum * currstr)
            else:
                currstr += s[i]
        
        return currstr
            

            
                

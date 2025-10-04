from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        ## Approach: Stack to handle operator precedence
        ## TC: O(n), SC: O(n)
        s = s.replace(" ", "")
        
        numStack = deque([])
        num = 0
        last_op = '+'
        i = 0

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            # If we see an operator or reach the end of string
            if not ch.isdigit() or i == len(s) - 1:
                if last_op == '+':
                    numStack.append(num)
                elif last_op == '-':
                    numStack.append(-num)
                elif last_op == '*':
                    numStack.append(numStack.pop() * num)
                elif last_op == '/':
                    prev = numStack.pop()
                    numStack.append(int(prev / num))

                last_op = ch
                num = 0

        return sum(numStack)
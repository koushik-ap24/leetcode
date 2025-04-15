class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []
        open_braces = ['(', '{', '[']
        close_braces = [')', '}', ']']

        for ch in s:
            if ch in open_braces:
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                brace = stack.pop()
                if open_braces.index(brace) != close_braces.index(ch):
                    return False
        
        if len(stack) > 0:
            return False
            
        return True
    
def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    
    stack = []
    open_braces = ['(', '{', '[']
    close_braces = [')', '}', ']']

    for ch in s:
        if ch in open_braces:
            stack.append(ch)
        elif len(stack) == 0:
            return False
        else:
            brace = stack.pop()
            if open_braces.index(brace) != close_braces.index(ch):
                return False
    
    if len(stack) > 0:
        return False
    
    return True

s = "(("
print(isValid(s))

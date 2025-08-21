class Solution:
    def smallestString(self, s: str) -> str:
        ## Greedy solution: modify as few 'a' chars as possible
        # Find the first non-'a' character and replace consecutive non-'a' characters until we reach an 'a' or the end
        # TC: O(n), SC: O(n)
        res = list(s)
        i = 0

        while i < len(s) and res[i] == 'a':
            i += 1
        
        if i == len(s):
            res[-1] = 'z'
        else:
            while i < len(s) and res[i] != 'a':
                res[i] = chr(ord(res[i]) - 1)
                i += 1
            
        return ''.join(res)
from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ## Approach: Use a hashmap to group characters by their row index
        ## TC: O(n), SC: O(n)
        
        if numRows == 1 or numRows >= len(s):
            return s

        rowMap = defaultdict(list)
        row = 1
        direction = 0 # 0 = down, 1 = up

        for ch in s:
            rowMap[row].append(ch)
            if row == 1:
                direction = 0
            elif row == numRows:
                direction = 1
            
            if direction == 0:
                row += 1
            else:
                row -= 1
        
        res = []
        for row in range(1, numRows+1):
            res += rowMap[row]
        
        return ''.join(res)
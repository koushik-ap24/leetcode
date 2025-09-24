class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i in range(len(columnTitle)-1, -1, -1):
            charNum = ord(columnTitle[i]) - ord('A') + 1
            res += pow(26, abs(i - (len(columnTitle) - 1))) * charNum
        
        return res
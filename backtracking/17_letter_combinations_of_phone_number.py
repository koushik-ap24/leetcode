from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Create a digit to character map
        if len(digits) == 0:
            return []
        
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # For each digit, we compute all possible combinations with that char in that index
        res = []
        combination = []
        def dfs(i):
        # When we go past the last digit, we have created a new combination, so add that to list of combinations
            if i == len(digits):
                res.append(''.join(combination))
                return
            
        # repeat for all chars for all digits
            letters = phoneMap[digits[i]]
        # We do not want to iterate through all chars since we do not want to consider anything except the first digit as the starting point
            for letter in letters:
                combination.append(letter)
                dfs(i+1)
                combination.pop()
             

        # return all combinations
        dfs(0)
        return res
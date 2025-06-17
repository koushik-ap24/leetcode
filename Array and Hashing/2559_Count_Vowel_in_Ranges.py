from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ## My approach:
        # TC: O(n + q), SC: O(n)
        # where n is the number of words and q is the number of queries.
        prefixArr = []
        vowelSet = {'a','e','i','o','u'}
        for i in range(len(words)):
            
            condition = words[i][0] in vowelSet and words[i][-1] in vowelSet
            
            if i == 0:
                num = 0 if not condition else 1
            else:
                num = prefixArr[i-1][0] if not condition else (prefixArr[i-1][0]+1)
            
            prefixArr.append((num, condition))

        res = []
        for start,end in queries:
            diff = prefixArr[end][0] - prefixArr[start][0]
            if prefixArr[start][1]:
                diff += 1
            
            res.append(diff)
        
        return res
        
        ## Another approach: Optimised in terms of space and lines of code
        # TC: O(n + q), SC: O(n)
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        
        # Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            if words[i][0] in vowelSet and words[i][-1] in vowelSet:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        # Answer the queries
        res = []
        for start, end in queries:
            res.append(prefix[end + 1] - prefix[start])
        
        return res

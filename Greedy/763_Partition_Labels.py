from typing import Counter, List

# Get Frequency of all chars in string.
# Linear scan - maintain set of encountered chars. If all encountered chars have been accounted for (duplicated included), add that as new substring.
# Repeat until all chars have been accounted for.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequency = Counter(s)
        res = []

        size = 0
        seen = set()
        for letter in s:
            if letter not in seen:
                seen.add(letter)
            
            frequency[letter] -= 1
            size += 1
            if frequency[letter] == 0:
                seen.remove(letter)
            
            if not seen:
                res.append(size)
                size = 0
        
        return res
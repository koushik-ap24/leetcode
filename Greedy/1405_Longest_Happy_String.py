import heapq

# Use max-heap to maintain char with most repetitions left
# Greedy as we always consider the most repeated char first, then consider the next if we cant use the first one
# Continue until
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        frequency = []
        if a:
            frequency.append((-a, "a"))
        if b:
            frequency.append((-b, "b"))
        if c:
            frequency.append((-c, "c"))
        
        heapq.heapify(frequency)

        res = ""
        reserve = None
        while frequency:
            numChar, char = heapq.heappop(frequency)
            if len(res) >= 2 and char == res[-1] and char == res[-2]:
                reserve = (numChar, char)
                continue
            
            res += char
            if reserve:
                heapq.heappush(frequency, reserve)
                reserve = None
            if numChar != -1:
                heapq.heappush(frequency, (numChar+1, char))
        
        return res
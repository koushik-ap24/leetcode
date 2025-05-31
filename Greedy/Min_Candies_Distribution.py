from typing import List

def candies(ratings: List[int]) -> int:
    ## 2-pass greedy approach
    # Each pass handles one direction of the neighbor constraint. 
    # The max() in Pass 2 ensures that if a position needs to satisfy both constraints (like a peak), it gets enough candies for the more demanding one.

    if len(ratings) == 0:
        return 0
    
    res = [1] * len(ratings)
    # First pass -> increasing sequences
    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            res[i] = res[i-1] + 1

    # First pass -> decreasing sequences
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            res[i] = max(res[i], res[i+1] + 1)
    
    
    return sum(res)
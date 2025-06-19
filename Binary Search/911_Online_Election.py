import bisect
from collections import defaultdict
from operator import itemgetter
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votes = defaultdict(int)
        maxCount = 0
        currWinner = 0
        self.winner = []
        for i in range(len(times)):
            votes[persons[i]] = votes.get(persons[i],0) + 1
            if votes[persons[i]] >= maxCount:
                currWinner = persons[i]
                maxCount = votes[persons[i]]
            self.winner.append((times[i], currWinner))
        

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.winner, t, key=itemgetter(0)) - 1
        return self.winner[idx][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
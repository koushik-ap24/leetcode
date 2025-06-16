from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        
        # Create counter for each letter for each position
        voteMap = {votes[0][i]: [0]*len(votes[0]) for i in range(len(votes[0]))}

        for vote in votes:
            for i in range(len(vote)):
                count = voteMap[vote[i]][i]
                voteMap[vote[i]][i] = count - 1
        
        sortedTeams = dict(sorted(voteMap.items(), key=lambda item: (item[1], item[0])))

        res = ""
        for team in sortedTeams:
            res += team
        
        return res
        

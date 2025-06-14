from collections import defaultdict
from typing import List
import heapq


class Twitter:
    ## Approach 1: Using a stack to store tweets and a map to track followers
    # More of a brute force solution, but it works for the constraints given
    def __init__(self):
       self.tweetStack = []
       self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetStack.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followMap.get(userId, set())
        followers.add(userId)
        res = []
        i = len(self.tweetStack) - 1
        while len(res) < 10 and i >= 0:
            if self.tweetStack[i][0] in followers:
                res.append(self.tweetStack[i][1])
            i -= 1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        # User A follows user B

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        # User A unfollows user B
    
    ## Approach 2: Using a heap to process tweets for given user in recent order
    # Make a heap of all tweets from the user and their followers
    # The count will be used to sort the tweets in the heap based on recency
    # We can then return the top 10 tweets from the heap
    def __init__(self):
       self.tweetMap = defaultdict(list)
       self.followMap = defaultdict(set)
       self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followMap.get(userId, set())
        followers.add(userId)
        res = []
        heap = []
        for follower in followers:
            heap += self.tweetMap[follower]
        
        heapq.heapify(heap)
        while heap and len(res) < 10:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        # User A follows user B

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        # User A unfollows user B

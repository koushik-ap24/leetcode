from collections import defaultdict
import heapq
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratingMap = defaultdict(tuple)
        self.cuisineMap = defaultdict(list)
        for i in range(len(foods)):
            self.ratingMap[foods[i]] = (-ratings[i], cuisines[i])
            heapq.heappush(self.cuisineMap[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.ratingMap[food][1]
        self.ratingMap[food] = (-newRating, cuisine)
        heapq.heappush(self.cuisineMap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while (self.cuisineMap[cuisine][0][0] != self.ratingMap[self.cuisineMap[cuisine][0][1]][0]):
            heapq.heappop(self.cuisineMap[cuisine])
        
        return self.cuisineMap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
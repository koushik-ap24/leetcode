from collections import deque
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Constraints:
        # target is always positive
        # speeds are all positive
        # positions are unique and less than target
        # Will have at least one car on highway (no empty array)

        # Approach:
        # Create an array of tuples (position, speed)
        cars = [(position[i], speed[i]) for i in range(len(position))]

        # Sort array in non increasing order
        cars.sort(key=lambda x:x[0], reverse=True)

        # Maintain a stack of distinct fleets
        fleets = deque([])

        # for each car in the array, calculate time to reach target
        for pos,spd in cars:
            time = (target-pos)/spd
        # if this is <= the car ahead, then merge fleets, otherwise this is a distinct fleet
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        
        # Return length of stack as the number of distinct fleets
        return len(fleets)

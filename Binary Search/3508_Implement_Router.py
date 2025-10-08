from collections import defaultdict, deque
from typing import List


class Router:
    def __init__(self, memoryLimit: int):
        self.packetQueue = deque()
        self.packetSet = set()
        self.destMap = defaultdict(deque)
        self.limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packetSet:
            return False

        self.packetQueue.append((source, destination, timestamp))
        self.destMap[destination].append(timestamp)
        self.packetSet.add((source, destination, timestamp))

        if len(self.packetQueue) > self.limit:
            oldSrc, oldDest, oldTime = self.packetQueue.popleft()
            self.destMap[oldDest].popleft()
            self.packetSet.discard((oldSrc, oldDest, oldTime))

        return True

    def forwardPacket(self) -> List[int]:
        if not self.packetQueue:
            return []

        src, dest, time = self.packetQueue.popleft()
        self.destMap[dest].popleft()
        self.packetSet.discard((src, dest, time))
        return [src, dest, time]

    def findPacket(self, packets, time, lower):
        left, right = 0, len(packets) - 1
        while left <= right:
            mid = (left + right) // 2
            if (packets[mid] >= time if lower else packets[mid] > time):
                right = mid - 1
            else:
                left = mid + 1
        return left if lower else right

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = self.destMap[destination]
        lower = self.findPacket(packets, startTime, True)
        upper = self.findPacket(packets, endTime, False)
        return max(0, upper - lower + 1)
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
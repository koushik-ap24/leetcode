from collections import defaultdict
import heapq


class StockPrice:

    def __init__(self):
        self.minPriceHeap = []
        self.maxPriceHeap = []
        self.latestTime = 0
        self.pricesMap = defaultdict(int)

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.minPriceHeap, (price, timestamp))
        heapq.heappush(self.maxPriceHeap, (-price, timestamp))
        self.pricesMap[timestamp] = price
        if self.latestTime < timestamp:
            self.latestTime = timestamp

    def current(self) -> int:
        return self.pricesMap[self.latestTime]

    def maximum(self) -> int:
        while ((-1 * self.maxPriceHeap[0][0]) != self.pricesMap[self.maxPriceHeap[0][1]]):
            heapq.heappop(self.maxPriceHeap)
        
        return self.maxPriceHeap[0][0] * -1

    def minimum(self) -> int:
        while ((self.minPriceHeap[0][0]) != self.pricesMap[self.minPriceHeap[0][1]]):
            heapq.heappop(self.minPriceHeap)
        
        return self.minPriceHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
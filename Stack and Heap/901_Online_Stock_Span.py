from collections import deque


class StockSpanner:
    ## Approach: Monotonic Stack
    ## Intuition: Keep a stack of (price, span) tuples in decreasing order of price and in order of arrival
    ## For each new price, pop from stack until we find a price greater than current price
    ## The span for the current price is 1 + sum of spans of all popped prices
    ## TC: O(n), SC: O(n) for the stack

    def __init__(self):
        self.stockPrice = deque([])

    def next(self, price: int) -> int:
        span = 1
        while len(self.stockPrice) and self.stockPrice[-1][0] <= price:
            _, stockSpan = self.stockPrice.pop()
            span += stockSpan
        
        self.stockPrice.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
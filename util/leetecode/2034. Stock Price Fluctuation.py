from sortedcontainers import SortedList

# sol2. priority queue + map
class StockPrice:
    def __init__(self):
        self.lowerPqueue = []
        self.upperPqueue = []
        self.orderbookMap = {}
        self.timestampNow = 0

    # 先推進去
    def update(self, timestamp: int, price: int) -> None:
        heappush(self.upperPqueue, (-price, timestamp))
        heappush(self.lowerPqueue, (price, timestamp))
        self.orderbookMap[timestamp] = price
        self.timestampNow = max(timestamp, self.timestampNow)

    def current(self) -> int:
        return self.orderbookMap[self.timestampNow]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.upperPqueue[0]
            if -price == self.orderbookMap[timestamp]:
                return -price
            heappop(self.upperPqueue)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.lowerPqueue[0]
            if price == self.orderbookMap[timestamp]:
                return price
            heappop(self.lowerPqueue) 

# sol1. sorted list + map 
# class StockPrice:

#     def __init__(self):
#         self.price = SortedList()
#         self.orderbookMap = {}
#         self.timestampNow = 0

#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp in self.orderbookMap:
#             self.price.discard(self.orderbookMap[timestamp])
#         self.price.add(price)
#         self.orderbookMap[timestamp] = price
#         self.timestampNow = max(timestamp, self.timestampNow)

#     def current(self) -> int:
#         return self.orderbookMap[self.timestampNow]

#     def maximum(self) -> int:
#         return self.price[-1]

#     def minimum(self) -> int:
#         return self.price[0]





# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
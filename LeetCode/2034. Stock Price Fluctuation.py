# 2034. Stock Price Fluctuation

# Solution 1: Correct in the first time - one improvement possible is to not use heap for max timestamp but a variable
# (Bit more cleaner solution with same logic from discussion - https://leetcode.com/problems/stock-price-fluctuation/discuss/1962912/Python3-using-min-and-max-heap.-Beats-99.39)
import heapq

class StockPrice:

    def __init__(self):
        self.time_price_map = dict()
        self.time_max_heap = []
        self.price_max_heap = []
        self.price_min_heap = []
        
        heapq.heapify(self.time_max_heap)
        heapq.heapify(self.price_max_heap)
        heapq.heapify(self.price_min_heap)
        
        self.wrong_price_map_max = dict()
        self.wrong_price_map_min = dict()

    def update(self, timestamp: int, price: int) -> None:
        # if new timestamp then insert it into timestamp heap otherwise it already exists
        if timestamp not in self.time_price_map:
            heapq.heappush(self.time_max_heap, -timestamp)
        else:
            old_price = self.time_price_map[timestamp]
            self.wrong_price_map_min[old_price] = self.wrong_price_map_min.get(old_price, 0) + 1
            self.wrong_price_map_max[-old_price] = self.wrong_price_map_max.get(-old_price, 0) + 1

        heapq.heappush(self.price_min_heap, price)
        heapq.heappush(self.price_max_heap, -price)    
        self.time_price_map[timestamp] = price

    def current(self) -> int:
        return self.time_price_map[-self.time_max_heap[0]]

    def maximum(self) -> int:
        while self.wrong_price_map_max.get(self.price_max_heap[0], None):
            wrong_price = heapq.heappop(self.price_max_heap)
            self.wrong_price_map_max[wrong_price] = self.wrong_price_map_max[wrong_price] - 1 if self.wrong_price_map_max[wrong_price] > 1 else 0
            
        return -self.price_max_heap[0]

    def minimum(self) -> int:
        while self.wrong_price_map_min.get(self.price_min_heap[0], None):
            wrong_price = heapq.heappop(self.price_min_heap)
            self.wrong_price_map_min[wrong_price] = self.wrong_price_map_min[wrong_price] - 1 if self.wrong_price_map_min[wrong_price] > 1 else 0
            
        return self.price_min_heap[0]


# Solution 2: Same as solution 1 but with the improvement of using var for current timestamp instead of heap. What was I thinking?
import heapq

class StockPrice:

    def __init__(self):
        self.time_price_map = dict()
        self.curr_ts = -1
        self.price_max_heap = []
        self.price_min_heap = []

        heapq.heapify(self.price_max_heap)
        heapq.heapify(self.price_min_heap)

        self.wrong_price_map_max = dict()
        self.wrong_price_map_min = dict()

    def update(self, timestamp: int, price: int) -> None:
        self.curr_ts = max(self.curr_ts, timestamp)

        if timestamp in self.time_price_map:
            old_price = self.time_price_map[timestamp]
            self.wrong_price_map_min[old_price] = self.wrong_price_map_min.get(old_price, 0) + 1
            self.wrong_price_map_max[-old_price] = self.wrong_price_map_max.get(-old_price, 0) + 1

        heapq.heappush(self.price_min_heap, price)
        heapq.heappush(self.price_max_heap, -price)
        self.time_price_map[timestamp] = price

    def current(self) -> int:
        return self.time_price_map[self.curr_ts]

    def maximum(self) -> int:
        while self.wrong_price_map_max.get(self.price_max_heap[0], None):
            wrong_price = heapq.heappop(self.price_max_heap)
            self.wrong_price_map_max[wrong_price] = self.wrong_price_map_max[wrong_price] - 1 if self.wrong_price_map_max[wrong_price] > 1 else 0

        return -self.price_max_heap[0]

    def minimum(self) -> int:
        while self.wrong_price_map_min.get(self.price_min_heap[0], None):
            wrong_price = heapq.heappop(self.price_min_heap)
            self.wrong_price_map_min[wrong_price] = self.wrong_price_map_min[wrong_price] - 1 if self.wrong_price_map_min[wrong_price] > 1 else 0

        return self.price_min_heap[0]
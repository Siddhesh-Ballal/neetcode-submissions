class MedianFinder:

    def __init__(self):
        self.smallheap = []      # maxheap
        self.largeheap = []      # minheap
        # both ~ roughly the same size -> only differ by atmost 1

    def addNum(self, num: int) -> None:
        # by default add to small heap (maxheap)
        heapq.heappush(self.smallheap, -num)
        if (self.smallheap and self.largeheap and -self.smallheap[0] > self.largeheap[0]) or (len(self.smallheap) > 1 + len(self.largeheap)):
            val = heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, -val)

        if len(self.largeheap) > 1 + len(self.smallheap):
            val = heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap, -val)

    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return -self.smallheap[0]
        
        if len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]

        return (self.largeheap[0] - self.smallheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
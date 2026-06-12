class MinHeap:
    
    def __init__(self):
        self.minheap = [0]

    def push(self, val: int) -> None:
        self.minheap.append(val)
        # percolate up
        i = len(self.minheap)-1
        while i > 1 and self.minheap[i//2] > self.minheap[i]:
            self.minheap[i//2], self.minheap[i] = self.minheap[i], self.minheap[i//2]
            i //= 2

    def pop(self) -> int:
        if len(self.minheap) <= 1: return -1
        if len(self.minheap) == 2: return self.minheap.pop()
        res = self.top() #!
        self.minheap[1] = self.minheap.pop()
        # percolate down
        i = 1
        while 2 * i < len(self.minheap):
            if 2*i+1 < len(self.minheap) and self.minheap[2*i+1] < self.minheap[2*i] and self.minheap[i] > self.minheap[2*i+1]:
                self.minheap[i], self.minheap[2*i+1] = self.minheap[2*i+1], self.minheap[i]
                i = 2*i+1
            elif self.minheap[i] > self.minheap[2*i]:
                self.minheap[i], self.minheap[2*i] = self.minheap[2*i], self.minheap[i]
                i = 2*i
            else:
                break
        return res

    def top(self) -> int:
        return self.minheap[1] if len(self.minheap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.minheap = [0] + nums
        # percolate down
        for i in reversed(range(1, len(self.minheap)//2+1)):
            while 2 * i < len(self.minheap):
                if 2*i+1 < len(self.minheap) and self.minheap[2*i+1] < self.minheap[2*i] and self.minheap[i] > self.minheap[2*i+1]:
                    self.minheap[i], self.minheap[2*i+1] = self.minheap[2*i+1], self.minheap[i]
                    i = 2*i+1
                elif self.minheap[i] > self.minheap[2*i]:
                    self.minheap[i], self.minheap[2*i] = self.minheap[2*i], self.minheap[i]
                    i = 2*i
                else:
                    break
            
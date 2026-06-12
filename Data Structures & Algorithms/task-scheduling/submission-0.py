class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Freqs = Counter(tasks)
        heap = [-freq for freq in Freqs.values()]
        heapq.heapify(heap)
        q = deque()
        t = 0
        while q or heap:
            t += 1
            if heap:
                f = heapq.heappop(heap)
                if 1 + f != 0: q.append([1 + f, t + n])
            if q and q[0][1] == t:
                f, e = q.popleft()
                heapq.heappush(heap, f)
        return t
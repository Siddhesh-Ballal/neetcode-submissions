class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {}
        
        neighbors = {}
        for i in range(n): neighbors[i] = []
        for source, destination, weight in edges: neighbors[source].append([destination, weight])

        minheap = [[0, src]]
        while minheap:
            minpath, vertex = heapq.heappop(minheap)
            if vertex in res: continue
            res[vertex] = minpath
            for destination, weight in neighbors[vertex]:
                if destination not in res:
                    heapq.heappush(minheap, [weight + minpath, destination])
        
        for i in range(n):
            if i not in res: res[i] = -1
            
        return res

class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst not in self.graph or src not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        q = deque()
        q.append(src)
        visited = set()
        visited.add(src)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == dst:
                    return True
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        return False
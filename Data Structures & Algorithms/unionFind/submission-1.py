class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.numberOfComponents = n
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if x!= self.par[x]:
            self.par[x] = self.find(self.par[x])       
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y) 

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2: return False

        if self.rank[p1] <= self.rank[p2]: self.par[p1] = p2
        if self.rank[p1] > self.rank[p2]: self.par[p2] = p1
        self.numberOfComponents -= 1

        return True

    def getNumComponents(self) -> int:
        return self.numberOfComponents
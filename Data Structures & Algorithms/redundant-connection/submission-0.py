class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        ran = [1 for i in range(n + 1)]

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            return par[i]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False
            if ran[p1] >= ran[p2]:
                ran[p1] += ran[p2]
                par[p2] = p1
            else:
                ran[p2] += ran[p1]
                par[p1] = p2
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2): return [n1, n2]
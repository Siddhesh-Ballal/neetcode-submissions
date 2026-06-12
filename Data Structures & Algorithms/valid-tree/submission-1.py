class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        vis = set()
        def dfs(n, p):
            if n in vis: return False
            vis.add(n)
            for nb in adj[n]:
                if nb == p: continue
                if not dfs(nb, n): return False
            return True
        
        if not dfs(0, -1): return False
        print(vis)
        return len(vis) == n
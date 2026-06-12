class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjmap = {i : [] for i in range(n)}
        for a, b in edges:
            adjmap[a].append(b)
            adjmap[b].append(a)
        
        vis = set()
        
        def dfs(node, prv):
            if node in vis: return False
            vis.add(node)
            for neighbor in adjmap[node]:
                if neighbor == prv: continue
                if not dfs(neighbor, node): return False
            return True
        
        if not dfs(0, -1): return False
        if len(vis) != n: return False
        return True
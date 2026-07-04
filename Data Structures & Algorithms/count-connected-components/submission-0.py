class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        visit = set()
        res=0

        def dfs(node,par):
            if node in visit:
                return 
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei,node)

        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                res+=1
                if len(visit)==n:
                    break
        return res
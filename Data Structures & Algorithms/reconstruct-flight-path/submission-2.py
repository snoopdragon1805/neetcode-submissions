class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = collections.defaultdict(list)
        for src,dest in tickets:
            if src not in adj:
                adj[src] = []
            heapq.heappush(adj[src],dest)
        res = []

        def dfs(src):
            while adj[src]:
                nextprt = heapq.heappop(adj[src])
                dfs(nextprt)
            res.append(src)
        dfs("JFK")
        return res[::-1]

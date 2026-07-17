class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        a, b = 0,0
        dp = {}
        def dfs(i,j, alice):
            nonlocal a
            nonlocal b
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            cur = max(piles[i]+dfs(i+1,j,not alice), piles[j]+dfs(i,j-1,not alice))
            if alice:
                a+= cur
            else:
                b+= cur
            dp[(i,j)] = cur
        
        dfs(0,0, True)
        return True if a>b else False
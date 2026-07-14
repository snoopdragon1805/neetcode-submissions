class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n==3:
            return 2
        dp={}
        def dfs(n):
            if n <= 4:
                return n
            if n in dp:
                return dp[n]
            curres = 0
            for i in range(1, n):
                curres = max(curres, i*dfs(n-i))
            dp[n] = curres
            return curres
        return dfs(n)  

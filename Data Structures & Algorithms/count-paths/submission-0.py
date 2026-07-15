class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]

        def dfs(i,j):
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            if i+1<m:
                res+=dfs(i+1,j)
            if j+1<n:
                res+=dfs(i,j+1)
            dp[i][j] = res
            return res
        
        return dfs(0,0)
            
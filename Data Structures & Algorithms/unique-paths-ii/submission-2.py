class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1]*m for _ in range(n)]
        
        def dfs(i,j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i==n-1 and j==m-1:
                return 1
            
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            if i+1<n:
                res+=dfs(i+1,j)
            if j+1<m:
                res+=dfs(i,j+1)
            
            dp[i][j] = res

            return res
        return dfs(0,0)
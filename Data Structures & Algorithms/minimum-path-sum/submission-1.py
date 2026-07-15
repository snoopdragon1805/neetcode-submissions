class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[-1]*m for _ in range(n)]

        def dfs(i,j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            if i == n or j == m:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = grid[i][j]+min(dfs(i+1,j), dfs(i,j+1))
            return dp[i][j]
            
        return dfs(0,0)
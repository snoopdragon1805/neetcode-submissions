class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[-1]*m for _ in range(n)]

        def dfs(i,j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            res = float('inf')
            if i+1<n:
                res = min(res, grid[i][j]+dfs(i+1,j))
            if j+1<m:
                res = min(res, grid[i][j]+dfs(i,j+1))
            dp[i][j] = res

            return res
        return dfs(0,0)
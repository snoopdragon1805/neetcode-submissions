class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            return 1+dfs(i,j+1)+dfs(i,j-1)+dfs(i+1,j)+dfs(i-1,j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxarea = max(maxarea,dfs(i,j))
        return maxarea
        
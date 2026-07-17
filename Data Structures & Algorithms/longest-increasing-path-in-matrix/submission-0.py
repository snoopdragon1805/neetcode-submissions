class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = {}
        choices = [
            [1,0],[-1,0],[0,1],[0,-1]
        ]

        def dfs(i,j,prev):
            if i<0 or j<0 or i==n or j == m or matrix[i][j]<=prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            res = 1
            for k,l in choices:
                res = max(res,1+dfs(i+k,j+l,matrix[i][j]))
            dp[(i,j)] = res
            return res

        for i in range(n):
            for j in range(m):
                dfs(i,j,-1)
        return max(dp.values())

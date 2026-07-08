class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n
        def dfs(cur):
            if cur>=n:
                return cur == n
            if cache[cur]!=-1:
                return cache[cur]
            cache[cur] = dfs(cur+1)+dfs(cur+2)
            return cache[cur]
        return dfs(0)
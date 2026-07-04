class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        premap = {i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            premap[crs].append(preq)

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for preq in premap[crs]:
                if not dfs(preq):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
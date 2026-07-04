class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        premap = {i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            premap[crs].append(preq)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if premap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visiting.add(crs)
            for preq in premap[crs]:
                if not dfs(preq):
                    return False
            visiting.remove(crs)
            premap[crs] = []
            if crs not in res:
                res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
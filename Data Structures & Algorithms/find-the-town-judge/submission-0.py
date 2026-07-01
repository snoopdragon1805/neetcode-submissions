class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map={}
        trusts = set()
        for t in trust:
            if t[1] not in trust_map:
                trust_map[t[1]] = []
            trust_map[t[1]].append(t[0])
            trusts.add(t[0])
        for i in trust_map:
            if len(trust_map[i])==n-1 and i not in trusts:
                return i
        return -1
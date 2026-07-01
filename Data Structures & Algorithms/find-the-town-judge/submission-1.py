class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [0]*n
        b = [0]*n

        for i in trust:
            a[i[0]-1]+=1
            b[i[1]-1]+=1
        
        for i in range(n):
            if a[i]==0 and b[i] == n-1:
                return i+1
        return -1
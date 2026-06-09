class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s,res=0,[]
        for i in operations:
            if i == "+":
                res.append(res[-1]+res[-2])
                s+=res[-1]
            elif i == "C":
                s-=res.pop()
            elif i == "D":
                res.append(2*res[-1])
                s+=res[-1]
            else:
                s+=int(i)
                res.append(int(i))
        return s
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in range(len(operations)):
                if operations[i] == "+":
                    print(res)
                    res.append(res[-1]+res[-2])
                elif operations[i] == "D":
                    res.append(2*int(res[-1]))
                elif operations[i] == "C":
                    res.pop(-1)
                else:
                    res.append(int(operations[i]))


        s=0
        print(res)
        for i in res:
            s+=int(i)
        return s

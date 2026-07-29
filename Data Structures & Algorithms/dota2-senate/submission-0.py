class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1=[]
        q2=[]
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                q1.append(i)
            else:
                q2.append(i)
        while q1 and q2:
            r = q1.pop(0)
            d = q2.pop(0)

            if r<d:
                q1.append(r+n)
            else:
                q2.append(d+n)
        
        return "Radiant" if q1 else "Dire"

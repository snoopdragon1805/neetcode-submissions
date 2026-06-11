class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        c1 = {}
        for i in t:
            c1[i] = c1.get(i,0)+1
        res,reslen = [-1,-1] , float("inf")
        have, need = 0,len(c1)
        l=0
        c2={}
        for r in range(len(s)):
            c = s[r]
            c2[c] = c2.get(s[r],0)+1

            if c in c1 and c2[c] == c1[c]:
                have+=1
            
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r]
                c2[s[l]] -=1

                if s[l] in c1 and c2[s[l]]< c1[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen!=float("inf") else ""
        
                
        
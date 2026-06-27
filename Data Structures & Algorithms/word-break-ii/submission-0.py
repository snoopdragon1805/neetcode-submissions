class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]

        n = len(s)

        def backtrack(i, cur):
            if i==n:
                if len(cur)>0:
                    res.append(" ".join(cur))
                return 

            for j in range(i,n):
                word = s[i:j+1]
                if word not in wordDict:
                    continue
                cur.append(word)
                backtrack(j+1,cur)
                cur.pop()

        backtrack(0,[])
        return res

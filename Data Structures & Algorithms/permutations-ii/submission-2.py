class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n = len(nums)
        count = Counter(nums)
        def backtrack(cur):
            if len(cur) == n:
                res.append(cur.copy())
                return
            for i in count:
                if count[i]!=0:
                    cur.append(i)
                    count[i]-=1
                    backtrack(cur)
                    cur.pop()
                    count[i]+=1
            
        backtrack([])
        return res
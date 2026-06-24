class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [val for val in range(1,n+1)]
        if n==k:
            return [arr]
        res=[]

        def dfs(i,subset):
            if len(subset)>k:
                return
            
            for j in range(i,len(arr)):
                subset.append(arr[j])
                if len(subset)==k:
                    res.append(subset.copy())
                dfs(j+1,subset)
                subset.pop()
        dfs(0,[])
        return res
        
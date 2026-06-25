class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        #n = len(nums)
        def backtrack(arr,cur):
            if len(arr)==0:
                if cur not in res:
                    res.append(cur.copy())
                    return
                return 
            for i in range(len(arr)):
                cur.append(arr[i])
                temp = arr.copy()
                temp.pop(i)
                backtrack(temp,cur)
                cur.pop()
        backtrack(nums,[])
        return res


            
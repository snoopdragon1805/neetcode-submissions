class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = []
        lt=0
        sum=0
        for i in nums:
            sum+=i
            prefix.append(sum)
        l=-1
        for r in range(len(prefix)):
            if prefix[r]<target:
                continue
            else:
                while prefix[r]-prefix[l+1]>=target:
                    l+=1            
                if lt==0:
                    lt = r-l
                else:
                    lt = min(lt,r-l)
        return lt
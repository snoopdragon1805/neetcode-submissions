class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s=0
        lt = float('inf')
        for r in range(len(nums)):
            s+=nums[r]
            while(s>=target):
                lt = min(lt,r-l+1)
                s-=nums[l]
                l+=1
        return lt if lt!=float('inf') else 0

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums = set(nums)
        
        for start in nums:
            if start-1 not in nums:
                end=start+1
                while(end in nums):
                    end+=1
                res = max(res,end-start)
        return res

        
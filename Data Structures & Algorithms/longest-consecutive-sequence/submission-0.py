class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        store = set(nums)
        
        for num in nums:
            streak=0
            current=num
            while current in nums:
                streak+=1
                current+=1
            res = max(res,streak)
        
        return res

        
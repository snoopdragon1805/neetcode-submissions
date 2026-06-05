class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        min=nums[0]
        for i in nums:
            if i < 1:
                continue
            if i < min:
                min=i
        if min<0 or min >1:
            return 1
        
        n = len(nums)
        i=1
        while(i<n):
            if min+1 in nums:
                min+=1
                i+=1
            else:
                return min+1
        return min+1

        
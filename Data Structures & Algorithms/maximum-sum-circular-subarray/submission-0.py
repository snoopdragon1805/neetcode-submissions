class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0,0
        total=0

        for i in nums:
            curMax = max(curMax+i,i)
            curMin = min(curMin+i,i)
            total+=i
            globalMax = max(globalMax,curMax)
            globalMin = min(globalMin,curMin)
        return max(globalMax, total-globalMin) if globalMax>0 else globalMax
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(curSum+nums[i], nums[i])
            res = max(res,curSum)
        return res
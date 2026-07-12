class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = -1e9
        for i in nums:
            temp = i*curMax
            curMax = max(i*curMax, i*curMin, i)
            curMin = min(temp, i*curMin, i)
            res = max(res, curMax)
        return res
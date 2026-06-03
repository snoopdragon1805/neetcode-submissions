class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        n = len(nums)
        for i in range(1,len(nums)):
            prefix.append(nums[i]*prefix[i-1])
            suffix.append(nums[n-i-1]*suffix[i-1])
        result=[]
        suffix.reverse()
        for i in range(n):
            if i == 0:
                result.append(suffix[i+1])
            elif i == n-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*suffix[i+1])

        return result
        
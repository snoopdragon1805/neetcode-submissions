class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k!=0:
            return False
        s = total//k

        arr = [0]*k
        nums.sort(reverse=True)
        def dfs(i):
            if i == len(nums):
                return True
            for side in range(k):
                if arr[side]+nums[i]<=s:
                    arr[side]+=nums[i]
                    if dfs(i+1):
                        return True
                    arr[side]-=nums[i]
                if arr[side]==0:
                    break
            return False

        return dfs(0)

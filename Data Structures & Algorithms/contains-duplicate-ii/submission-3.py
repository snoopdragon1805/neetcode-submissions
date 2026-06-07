class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            j=i+1
            while j<n and abs(i-j)<=k:
                if nums[i] == nums[j]:
                    return True
                j+=1
        return False

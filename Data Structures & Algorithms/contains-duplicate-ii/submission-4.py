class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        seen=set()

        for num in nums:
            if len(seen)>k:
                seen.remove(nums[i])
                i+=1
            if num in seen:
                return True
            seen.add(num)
        return False
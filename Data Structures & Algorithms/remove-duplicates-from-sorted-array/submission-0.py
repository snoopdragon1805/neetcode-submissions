class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ordered = list(dict.fromkeys(nums))
        nums[:] = ordered
        return len(nums)
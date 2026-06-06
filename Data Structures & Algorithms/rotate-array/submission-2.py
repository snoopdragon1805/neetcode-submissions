class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #res=[]
        k%=len(nums)
        res=nums[len(nums)-k:]
        res+=nums[:len(nums)-k]
        nums[:]=res
        
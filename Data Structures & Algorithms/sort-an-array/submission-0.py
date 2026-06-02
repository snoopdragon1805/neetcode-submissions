class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        left_sorted = self.mergeSort(left)
        right_sorted = self.mergeSort(right)

        return self.merge(left_sorted,right_sorted)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
            
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
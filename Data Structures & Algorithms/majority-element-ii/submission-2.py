from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res=[]
        n = len(nums)//3
        for key,value in count.items():
            if value>n:
                res.append(key)

        return res
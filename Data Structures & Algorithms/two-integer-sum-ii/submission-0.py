class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(numbers)):
            if target-numbers[i] in numbers and numbers.index(target-numbers[i])!=i:
                res=[i+1,numbers.index(target-numbers[i])+1]
                return res
        return res


        
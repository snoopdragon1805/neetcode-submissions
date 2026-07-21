class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        res = 1
        cur = 1
        greater = None

        for i in range(len(arr)-1):
            if greater == None:
                cur+=1
                if arr[i]>arr[i+1]:
                    greater = False
                elif arr[i] < arr[i+1]:
                    greater = True
                else:
                    cur = 1
            elif greater:
                if arr[i]>arr[i+1]:
                    cur+=1
                    greater = False
                else:
                    cur = 2 if arr[i] < arr[i+1] else 1
                    greater = True if arr[i] < arr[i+1] else None
            else:
                if arr[i]<arr[i+1]:
                    cur+=1
                    greater = True
                else:
                    cur = 2 if arr[i] > arr[i+1] else 1
                    greater = False if arr[i] > arr[i+1] else None
            res = max(res,cur)
        return res

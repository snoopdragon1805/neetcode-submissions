class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        l,r = 1,length-2
        while l<=r:
            m = (l+r)//2
            left,mid,right = get(m-1), get(m), get(m+1)
            if left<mid<right:
                l = m + 1
            elif left>mid>right:
                r = m-1
            else:
                break
        peak = m

        def binSearch(l,r,asc):
            while(l<=r):
                m = (l+r)//2
                val = get(m)
                if val == target:
                    return m
                if asc == (val<target):
                    l = m+1
                else:
                    r = m-1
            return -1

        res = binSearch(0,peak,True)
        return res if res!=-1 else binSearch(peak,length-1,False)

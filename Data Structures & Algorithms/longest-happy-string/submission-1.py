class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        for count,char in [[-a,'a'],[-b,'b'],[-c,'c']]:
            if count!=0:
                heapq.heappush(heap,[count,char])
        res=""
        prev=None
        while heap:
            val,ch = heapq.heappop(heap)
        
            if len(res)>1 and res[-1]==res[-2] == ch:
                if not heap:
                    break
                val2,ch2 = heapq.heappop(heap)
                res+=ch2
                val2+=1
                if val2:
                    heapq.heappush(heap,[val2,ch2])
                heapq.heappush(heap,[val,ch])
            else:
                res+=ch
                val+=1
                if val:
                    heapq.heappush(heap,[val,ch])
        return res

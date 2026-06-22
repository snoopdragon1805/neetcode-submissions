class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        heap=[]
        curpass=0

        for n,s,e in trips:
            while heap and heap[0][0]<=s:
                curpass-=heapq.heappop(heap)[1]
            curpass+=n
            if curpass>capacity:
                return False
            heapq.heappush(heap,[e,n])
        return True

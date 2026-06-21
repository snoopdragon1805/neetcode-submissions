class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-val,idx) for idx,val in count.items()]
        heapq.heapify(heap)
        prev = None
        res=''
        while heap or prev:
            if prev and not heap:
                return ""
            val,idx = heapq.heappop(heap)
            res+=idx
            val+=1

            if prev:
                heapq.heappush(heap,prev)
                prev = None

            if val!=0:
                prev = (val,idx)
        return res            
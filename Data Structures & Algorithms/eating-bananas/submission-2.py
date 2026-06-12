class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        low = 1
        high = m
        res = m
        while low<=high:
            k = low + ((high-low)//2)
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/k)
            if time<=h:
                res = k
                high = k-1
            else:
                low = k+1

        return res
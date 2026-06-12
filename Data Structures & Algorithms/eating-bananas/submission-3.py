class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        while low<high:
            k = low + ((high-low)//2)
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/k)
            if time<=h:
                high=k
            else:
                low = k+1
        return low
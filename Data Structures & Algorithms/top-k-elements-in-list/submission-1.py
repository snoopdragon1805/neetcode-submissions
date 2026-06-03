class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0)+1
        
        ans = sorted(map,key = map.get, reverse=True)
        return ans[:k]
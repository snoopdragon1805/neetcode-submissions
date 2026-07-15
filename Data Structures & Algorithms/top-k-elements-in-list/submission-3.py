class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0)+1
        ans = list(sorted(map.items(), key = lambda item: item[1], reverse = True))
        return [item[0] for item in ans[:k]]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0)+1
        
        sorted_by_value = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        ans=[]
        for i in sorted_by_value:
            if len(ans) ==k:
                return ans
            ans.append(i)
        return ans
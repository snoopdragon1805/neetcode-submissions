class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefix=0
        count=0
        for i in nums:
            prefix+=i

            if prefix-k in freq:
                count+=freq[prefix-k]
            freq[prefix] = freq.get(prefix,0)+1
        return count
